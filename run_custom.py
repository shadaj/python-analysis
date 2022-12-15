from instrumentation.data_tracing_receiver import DataTracingReceiver
from instrumentation.module_loader import PatchingPathFinder
from gnn.predict import evaluate

from instrumentation.helper import IntToClassMapping

patcher = PatchingPathFinder()
patcher.install()

receiver = DataTracingReceiver()

def predict():
  global receiver
  import numpy as np
  (allNodeDetails, allEdgeDetails, nodeEdgeCounts), times = receiver.receiverData
  def flatten(lol):
    return [i for l in lol for i in l]
  allNodeDetails = np.asarray(flatten(allNodeDetails))
  allEdgeDetails = np.reshape(np.asarray(flatten(allEdgeDetails)), (-1, 4))
  labels = [-1, 0]
  nodeEdgeCounts = np.concatenate([np.asarray(nodeEdgeCounts), np.expand_dims(np.asarray(labels), axis=1)], axis=1)
  patcher.uninstall()
  print("GNN Predicts this as: ", IntToClassMapping[evaluate(allNodeDetails, allEdgeDetails, nodeEdgeCounts)[0]])
  patcher.install()


def testWildImpl():
  import custom
  import numpy as np

  # Generate an input
  length = np.random.randint(3, 10)
  a = np.random.random(size=length).tolist()

  with receiver:
    # Call the custom function within the context manager
    ans = custom.my_function(a)
  predict()

testWildImpl()

patcher.uninstall()