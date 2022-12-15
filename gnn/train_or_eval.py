# Copyright 2020 DeepMind Technologies Limited.


# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# https://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Original implementation obtained from:
# https://github.com/deepmind/jraph/blob/master/jraph/ogb_examples/train.py
# This file has been modified from the original version above 

import functools
import logging
import pathlib
import pickle
from absl import app
from absl import flags
import haiku as hk
import jax
import jax.numpy as jnp
import jraph
from jraph._src import utils
import optax
import numpy as np
from data_load import get_graph, setEval, get_graph_test, read_train_data, read_eval_data

# from jax.config import config
# config.update("jax_debug_nans", True)

enable_jit = True

flags.DEFINE_string('model_name', 'model', 'Name of the .pkl file for the saved parameters (.pkl extension added automatically).')
flags.DEFINE_string('data_path', 'data', 'Directory of the data.')
flags.DEFINE_string('save_dir', 'model', 'Directory to save parameters to, or where to fetch parameters from for evaluation.')
flags.DEFINE_integer('batch_size', 40, 'Number of graphs in batch. Only used in training mode.')
flags.DEFINE_integer('num_epochs', 20, 'Number of training steps. Only used in training mode.')
flags.DEFINE_enum('mode', 'evaluate', ['train', 'evaluate'], 'Train or evaluate.')
flags.DEFINE_enum('testMode', 'test', ['test', 'testL', 'testLL'], 'What size dataset to evaluate on. Only required in evaluate mode.')
FLAGS = flags.FLAGS
num_classes = 46

hidden_dim = 512

def edge_update_fn(edges: jnp.ndarray, sent: jnp.ndarray, receive: jnp.ndarray, glob: jnp.ndarray) -> jnp.ndarray:
  """Edge update function for graph net."""
  net = hk.Sequential(
      [hk.Linear(hidden_dim), jax.nn.relu,
       hk.Linear(hidden_dim)])
  return net(jnp.concatenate([edges, sent, receive, glob], axis=1))


def node_update_fn(nodes: jnp.ndarray, sent: jnp.ndarray, receive: jnp.ndarray, glob: jnp.ndarray) -> jnp.ndarray:
  """Node update function for graph net."""
  net = hk.Sequential(
      [hk.Linear(hidden_dim), jax.nn.relu,
       hk.Linear(hidden_dim)])
  return net(jnp.concatenate([nodes, sent, receive, glob], axis=1))


def update_global_fn(nodes: jnp.ndarray, edges: jnp.ndarray, glob: jnp.ndarray) -> jnp.ndarray:
  """Global update function for graph net."""
  global num_classes
  # Molhiv is a binary classification task, so output pos neg logits.
  net = hk.Sequential(
      [hk.Linear(hidden_dim), jax.nn.relu,
       hk.Linear(num_classes)])
  return net(jnp.concatenate([nodes, edges, glob], axis=1))


def net_fn(graph: jraph.GraphsTuple) -> jraph.GraphsTuple:
  """Graph net function."""
  global num_classes
  # Add a global paramater for graph classification.
  graph = graph._replace(globals=jnp.zeros([graph.n_node.shape[0], num_classes]))
  embedder = jraph.GraphMapFeatures(
      hk.Linear(hidden_dim), hk.Linear(hidden_dim), hk.Linear(hidden_dim))
  net = jraph.GraphNetwork(
      update_node_fn=node_update_fn,
      update_edge_fn=edge_update_fn,
      update_global_fn=update_global_fn,
      aggregate_nodes_for_globals_fn=utils.segment_mean,
      aggregate_edges_for_globals_fn=utils.segment_mean
  )
  return net(embedder(graph))


def _nearest_bigger_power_of_two(x: int) -> int:
  """Computes the nearest power of two greater than x for padding."""
  y = 2
  while y < x:
    y *= 2
  return y


def pad_graph_to_nearest_power_of_two(
    graphs_tuple: jraph.GraphsTuple) -> jraph.GraphsTuple:
  """Pads a batched `GraphsTuple` to the nearest power of two.

  For example, if a `GraphsTuple` has 7 nodes, 5 edges and 3 graphs, this method
  would pad the `GraphsTuple` nodes and edges:
    7 nodes --> 8 nodes (2^3)
    5 edges --> 8 edges (2^3)

  And since padding is accomplished using `jraph.pad_with_graphs`, an extra
  graph and node is added:
    8 nodes --> 9 nodes
    3 graphs --> 4 graphs

  Args:
    graphs_tuple: a batched `GraphsTuple` (can be batch size 1).

  Returns:
    A graphs_tuple batched to the nearest power of two.
  """
  # Add 1 since we need at least one padding node for pad_with_graphs.
  pad_nodes_to = _nearest_bigger_power_of_two(jnp.sum(graphs_tuple.n_node)) + 1
  pad_edges_to = _nearest_bigger_power_of_two(jnp.sum(graphs_tuple.n_edge))
  # Add 1 since we need at least one padding graph for pad_with_graphs.
  # We do not pad to nearest power of two because the batch size is fixed.
  pad_graphs_to = graphs_tuple.n_node.shape[0] + 1
  return jraph.pad_with_graphs(graphs_tuple, pad_nodes_to, pad_edges_to,
                               pad_graphs_to)


def compute_loss(params, graph, label, net):
  """Computes loss."""
  global num_classes
  pred_graph = net.apply(params, graph)
  preds = jax.nn.log_softmax(pred_graph.globals, axis=1)
  targets = jax.nn.one_hot(label, num_classes)

  # Since we have an extra 'dummy' graph in our batch due to padding, we want
  # to mask out any loss associated with the dummy graph.
  # Since we padded with `pad_with_graphs` we can recover the mask by using
  # get_graph_padding_mask.
  mask = jraph.get_graph_padding_mask(pred_graph)

  # Cross entropy loss.
  loss = -jnp.mean(preds * targets * mask[:, None])
  correct, total = jnp.sum(
      (jnp.argmax(preds, axis=1) == label) * mask), jnp.sum(mask)
  return loss, (correct, total)

# cm = np.zeros(shape=(num_classes, num_classes))
def compute_loss_(params, graph, label, net):
  # global cm
  """Computes loss."""
  global num_classes
  pred_graph = net.apply(params, graph)
  preds = jax.nn.log_softmax(pred_graph.globals, axis=1)
  targets = jax.nn.one_hot(label, num_classes)

  # Since we have an extra 'dummy' graph in our batch due to padding, we want
  # to mask out any loss associated with the dummy graph.
  # Since we padded with `pad_with_graphs` we can recover the mask by using
  # get_graph_padding_mask.
  mask = jraph.get_graph_padding_mask(pred_graph)

  # Cross entropy loss.
  loss = -jnp.mean(preds * targets * mask[:, None])
  # Accuracy taking into account the mask
  correct, total = jnp.sum(
      (jnp.argmax(preds, axis=1) == label) * mask), jnp.sum(mask)

  lim = np.array(jnp.sum(mask)).item()
  np_targets = np.array(jnp.argmax(preds, axis=1))[:lim]
  np_labels = np.array(label)[:lim]
  # cm += confusion_matrix(np_labels, np_targets, labels=list(range(num_classes)))
  return loss, (correct, total)


def train(data_path, batch_size,
          num_epochs, save_dir, model_name):
  """OGB Training Script."""
  # Initialize the dataset reader.
  num_training_samples = read_train_data(data_path, batch_size)

  # Transform impure `net_fn` to pure functions with hk.transform.
  net = hk.without_apply_rng(hk.transform(net_fn))
  # Get a candidate graph and label to initialize the network.
  # REMOVED
  #graph, _ = reader.get_graph_by_idx(0)
  # /REMOVED
  graph, label = get_graph()

  num_training_steps = num_training_samples * num_epochs // batch_size
  print("###################################################################################################################")
  print("Training scheduled for %d epochs, which for %d training samples and batch size of %d will run for %d steps."
  %(num_epochs, num_training_samples, batch_size, num_training_steps))
  print("###################################################################################################################")
    

  # Initialize the network.
  logging.info('Initializing network.')
  params = net.init(jax.random.PRNGKey(636), graph)
  # Initialize the optimizer.
  opt_init, opt_update = optax.adam(optax.exponential_decay(init_value=1e-4, transition_steps=num_training_steps // 4, decay_rate=0.5, staircase=True))
  opt_state = opt_init(params)

  compute_loss_fn = functools.partial(compute_loss, net=net)
  # We jit the computation of our loss, since this is the main computation.
  # Using jax.jit means that we will use a single accelerator. If you want
  # to use more than 1 accelerator, use jax.pmap. More information can be
  # found in the jax documentation.
  compute_loss_fn = (
    # jax.jit
  jax.value_and_grad(
      compute_loss_fn, has_aux=True))
  if enable_jit:
    compute_loss_fn = jax.jit(compute_loss_fn)

  try:
    for idx in range(num_training_steps):
      # REMOVED
      #graph, label = next(reader)
      # /REMOVED
      graph, label = get_graph()

      # Jax will re-jit your graphnet every time a new graph shape is encountered.
      # In the limit, this means a new compilation every training step, which
      # will result in *extremely* slow training. To prevent this, pad each
      # batch of graphs to the nearest power of two. Since jax maintains a cache
      # of compiled programs, the compilation cost is amortized.
      graph = pad_graph_to_nearest_power_of_two(graph)

      # Since padding is implemented with pad_with_graphs, an extra graph has
      # been added to the batch, which means there should be an extra label.
      label = jnp.concatenate([label, jnp.array([0])])

      (loss, (cor, tot)), grad = compute_loss_fn(params, graph, label)
      # print("grad")
      # print(grad)
      updates, opt_state = opt_update(grad, opt_state, params)
      params = optax.apply_updates(params, updates)
      if idx % 1 == 0:
        logging.info('step: %s, loss: %s, acc: %s', idx, loss, cor/tot)
      if idx % 1000 == 0:
        if save_dir is not None:
          with pathlib.Path(save_dir, '%s%d.pkl'%(model_name, idx)).open('wb') as fp:
            logging.info('Saving Epoch %d model to %s', idx // 1125, save_dir)
            pickle.dump(params, fp)
  except:
    logging.info("Training stopped early")
  if save_dir is not None:
    with pathlib.Path(save_dir, '%s.pkl'%model_name).open('wb') as fp:
      logging.info('Saving model to %s', save_dir)
      pickle.dump(params, fp)
  logging.info('Training finished')


def evaluate(data_path, save_dir, model_name, test_mode):
  """Evaluation Script."""
    # Initialize the dataset reader.
  read_eval_data(test_mode, data_path)
  logging.info('Evaluating the model')
  # Transform impure `net_fn` to pure functions with hk.transform.
  net = hk.without_apply_rng(hk.transform(net_fn))
  # Get a candidate graph and label to initialize the network.
  with pathlib.Path(save_dir, '%s.pkl'%model_name).open('rb') as fp:
    params = pickle.load(fp)
  accumulated_loss = 0
  accumulated_cor = 0
  accumulated_tot = 0
  idx = 0

  # We jit the computation of our loss, since this is the main computation.
  # Using jax.jit means that we will use a single accelerator. If you want
  # to use more than 1 accelerator, use jax.pmap. More information can be
  # found in the jax documentation.
  compute_loss_fn = (
  # jax.jit
  functools.partial(compute_loss, net=net))
  if enable_jit:
    compute_loss_fn = jax.jit(compute_loss_fn)
  
  setEval()
  while True:
    s = get_graph_test()
    graph, label = s
    if graph is None:
      break


    # Jax will re-jit your graphnet every time a new graph shape is encountered.
    # In the limit, this means a new compilation every training step, which
    # will result in *extremely* slow training. To prevent this, pad each
    # batch of graphs to the nearest power of two. Since jax maintains a cache
    # of compiled programs, the compilation cost is amortized.
    graph = pad_graph_to_nearest_power_of_two(graph)

    # Since padding is implemented with pad_with_graphs, an extra graph has
    # been added to the batch, which means there should be an extra label.
    label = jnp.concatenate([label, jnp.array([-1])])
    loss, (cor,tot) = compute_loss_fn(params, graph, label)
    accumulated_cor += cor
    accumulated_tot += tot
    accumulated_loss += loss
    idx += 1
    if idx % 1 == 0:
      logging.info('Evaluated %s graphs', idx)
      logging.info('Cumulative Acc: %f', accumulated_cor / accumulated_tot)
      logging.info('Cumulative Cor: %f', accumulated_cor)
      logging.info('Cumulative Tot: %f', accumulated_tot)
  logging.info('Completed evaluation.')
  loss = accumulated_loss / idx
  accuracy = accumulated_cor / accumulated_tot
  logging.info('Eval loss: %s, accuracy %s', loss, accuracy)
  return loss, accuracy


def main(_):
  # global cm
  if FLAGS.mode == 'train':
    train(FLAGS.data_path, 
          FLAGS.batch_size, FLAGS.num_epochs, FLAGS.save_dir, FLAGS.model_name)
  elif FLAGS.mode == 'evaluate':
    evaluate(FLAGS.data_path, 
              FLAGS.save_dir, FLAGS.model_name, FLAGS.testMode)
    # print(cm)
    # np.save("confusion.npy", cm)
if __name__ == '__main__':
  app.run(main)
