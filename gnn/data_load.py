import jraph
import numpy as np
from pathlib import Path

partitions = 15
samples_per_partition = None
batch_size = None

nodes = []
edges = []
index = []

def read_train_data(data_path, bsize):
    global nodes, edges, index, samples_per_partition, batch_size
    batch_size = bsize
    path = Path(data_path if data_path is not None else "")
    for i in range(partitions):
        nodes.append(np.load(path / 'train' / str(i+1) / 'nodestrain.npy'))
        edges.append(np.load(path / 'train' / str(i+1) / 'edgestrain.npy'))
        index.append(np.load(path / 'train' / str(i+1) / 'indextrain.npy'))
    samples_per_partition = index[dataset_i].shape[0]-1
    return samples_per_partition * partitions

nodes_ = []
edges_ = []
index_ = []
def read_eval_data(testMode, data_path):
    global nodes_, edges_, index_, samples_per_partition
    path = Path(data_path if data_path is not None else "")
    for i in range(partitions):
        nodes_.append(np.load(path / testMode / str(i+1) / ('nodes%s.npy'%testMode)))
        edges_.append(np.load(path / testMode / str(i+1) / ('edges%s.npy'%testMode)))
        index_.append(np.load(path / testMode / str(i+1) / ('index%s.npy'%testMode)))
    samples_per_partition = index_[dataset_i].shape[0]-1

    

i = 0
dataset_i = 0
evalMode = False
epoch = 0

def reset():
    global i, dataset_i
    i = 0
    dataset_i = 0

def setEval():
    global evalMode
    evalMode = True

def getnparray(raw):
    ret = np.atleast_2d(np.asarray(raw))
    if ret.size == 0:
        return np.zeros(shape=(0, 1))
    else:
        return ret

def getnparray2(raw):
    ret = np.asarray(raw, dtype=np.int64)
    if ret.size == 0:
        return np.zeros(shape=(0), dtype=np.int64)
    else:
        return ret

def get_graph():
    global i, evalMode, dataset_i, epoch
    graphs = []
    labels = []
    for b in range(batch_size):
        sln = slice(index[dataset_i][i,0], index[dataset_i][i+1,0])
        sle = slice(index[dataset_i][i,1], index[dataset_i][i+1,1])
        label = np.asarray([index[dataset_i][i+1][2]])
        curGraphNodes = nodes[dataset_i][sln]
        curGraphEdges = edges[dataset_i][sle]
        if evalMode and not (i + 1) % (index[dataset_i].shape[0]-1):
            return None
        all_nodes = curGraphNodes[:,2:].astype('float64')
        all_edges = curGraphEdges[:,3:].astype('float64')
        all_senders = np.atleast_1d(curGraphEdges.astype('int64')[:,0].squeeze())
        all_receivers = np.atleast_1d(curGraphEdges.astype('int64')[:,1].squeeze())
        red_nodes = np.asarray([i for i in all_nodes]) # if i[-1] == 0])
        red_edges, red_sender, red_receiver = [], [], []
        for edge, sender, receiver in zip(all_edges, all_senders, all_receivers):
            #if edge[-1] == 0:
                red_edges.append(edge)
                red_sender.append(sender)
                red_receiver.append(receiver)
        red_edges = getnparray(red_edges)
        red_sender = getnparray2(red_sender)
        red_receiver = getnparray2(red_receiver)
        n_node = np.array([red_nodes.shape[0]]).astype('int64')
        n_edge = np.array([red_edges.shape[0]]).astype('int64')
        gr = jraph.GraphsTuple(
            nodes = red_nodes,
            edges = red_edges,
            n_node = n_node,
            n_edge = n_edge,
            senders = red_sender,
            receivers = red_receiver,
            globals = {}
        )
        i = (i + 1) % (index[dataset_i].shape[0]-1)
        if i == 0:
            dataset_i = (dataset_i + 1) % partitions
            if dataset_i == 0:
                epoch += 1
                print("######################\nNEW EPOCH: ", epoch)
            print("Starting New Dataset Partition ", dataset_i)
        graphs.append(gr)
        labels.append(label)
    return jraph.batch(graphs), np.concatenate(labels, axis=0)

def get_graph_test():
    global i, evalMode, dataset_i
    graphs = []
    labels = []
    for b in range(1):
        sln = slice(index_[dataset_i][i,0], index_[dataset_i][i+1,0])
        sle = slice(index_[dataset_i][i,1], index_[dataset_i][i+1,1])
        label = np.asarray([index_[dataset_i][i+1][2]])
        curGraphNodes = nodes_[dataset_i][sln]
        curGraphEdges = edges_[dataset_i][sle]
        all_nodes = curGraphNodes[:,2:].astype('float64')
        all_edges = curGraphEdges[:,3:].astype('float64')
        all_senders = np.atleast_1d(curGraphEdges.astype('int64')[:,0].squeeze())
        all_receivers = np.atleast_1d(curGraphEdges.astype('int64')[:,1].squeeze())
        red_nodes = np.asarray([i for i in all_nodes]) # if i[-1] == 0])
        red_edges, red_sender, red_receiver = [], [], []
        for edge, sender, receiver in zip(all_edges, all_senders, all_receivers):
            #if edge[-1] == 0:
                red_edges.append(edge)
                red_sender.append(sender)
                red_receiver.append(receiver)
        red_edges = getnparray(red_edges)
        red_sender = getnparray2(red_sender)
        red_receiver = getnparray2(red_receiver)
        n_node = np.array([red_nodes.shape[0]]).astype('int64')
        n_edge = np.array([red_edges.shape[0]]).astype('int64')
        gr = jraph.GraphsTuple(
            nodes = red_nodes,
            edges = red_edges,
            n_node = n_node,
            n_edge = n_edge,
            senders = red_sender,
            receivers = red_receiver,
            globals = {}
        )
        i = (i + 1) % (index_[dataset_i].shape[0]-1)
        if i == 0:
            dataset_i = dataset_i + 1
            if dataset_i == partitions:
                print("Finished all partitions")
                return None, None
            print("Starting New Dataset Partition ", dataset_i)
        graphs.append(gr)
        labels.append(label)
    return jraph.batch(graphs), np.concatenate(labels, axis=0)

