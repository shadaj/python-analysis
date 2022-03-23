from typing import Any, Dict, List, Tuple, Union, Optional
from typing_extensions import Literal

from .heap_object_tracking import HeapObjectTracker

from .data_tracing_variables import *

import networkx as nx
import matplotlib.pyplot as plt

import copy

from .helper import printDebug

generatedGraphs = 0

def add_dependency(child: Union[SymbolicElement, StackElement], parent: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent: ", str(parent))
  child.heap_elem = parent.heap_elem
  add_dependency_internal([(child, parent)])

def add_dependency2(child: Union[SymbolicElement, StackElement], parent1: Union[SymbolicElement, StackElement], parent2: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent1: ", str(parent1))
  printDebug("Parent2: ", str(parent2))
  add_dependency_internal([(child, parent1), (child, parent2)])

def add_dependency3(child: Union[SymbolicElement, StackElement], parent1: Union[SymbolicElement, StackElement], parent2: Union[SymbolicElement, StackElement], parent3: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent1: ", str(parent1))
  printDebug("Parent2: ", str(parent2))
  printDebug("Parent3: ", str(parent3))
  add_dependency_internal([(child, parent1), (child, parent2), (child, parent3)])

allObservedPositions = set()
variableToLatestVersion = {}

G = nx.MultiDiGraph()
dependencyCount = 0

allNodeDetails = []
allEdgeDetails = []
nodeEdgeCounts = [(0,0)]
edgeCounter = 0
edgeMap = {}

def add_dependency_internal(depList: List[Tuple[Union[SymbolicElement, StackElement], Union[SymbolicElement, StackElement]]]) -> None:
  global allObservedPositions, edgeCounter, edgeMap
  if len(depList) == 2:
    assert depList[0][0] == depList[1][0], "Same child must be present in all dependencies"
  if len(depList) == 3:
    assert depList[0][0] == depList[1][0] == depList[2][0], "Same child must be present in all dependencies"

  child = depList[0][0]
  newChildVersion = 1 + max(max([dep[0].version for dep in depList]), max([dep[1].version for dep in depList]))
  child.version = newChildVersion
  childStr = child.var_name + "#" + str(child.version)

  oldChildVersion = variableToLatestVersion.get(child.var_name, None)
  variableToLatestVersion[child.var_name] = child.version

  G.add_node(childStr, pos=(child.var_name, child.version))

  if oldChildVersion is not None:
    oldChildStr = child.var_name + "#" + str(oldChildVersion)
    edgeCounter += 1
    param = len(G.get_edge_data(oldChildStr, childStr, default={}))
    edgeMap[(oldChildStr, childStr, param)] = edgeCounter
    G.add_edge(oldChildStr, childStr, sameVariableEdge = True)

  allObservedPositions.add(child.var_name)

  for dep in depList:
    parent = dep[1]
    parentStr = parent.var_name + "#" + str(parent.version)

    G.add_node(parentStr, pos=(parent.var_name, parent.version))
    edgeCounter += 1
    param = len(G.get_edge_data(parentStr, childStr, default={}))
    edgeMap[(parentStr, childStr, param)] = edgeCounter
    G.add_edge(parentStr, childStr, sameVariableEdge = False)

    variableToLatestVersion[parent.var_name] = parent.version

    allObservedPositions.add(parent.var_name)

def generate_memory_graph():
  global allObservedPositions, G, dependencyCount, variableToLatestVersion, generatedGraphs, object_id_to_heap_element_map, edgeMap, edgeCounter
  maxIndex = 0
  positionStrToXcoord = {}
  for positionStr in sorted(allObservedPositions, reverse=False):
    positionStrToXcoord[positionStr] = maxIndex
    maxIndex += 1
  
  plt.subplot(121)

  toRemove = []
  allNodes = [h for h in G.nodes]

  # Pruning extra nodes. Any node which does not have "nameless" in it's name, i.e. is not a compound data structure (non primitive like int/str) 
  # is treated as a node to exclude. This is a temporary logic and can be changed in the future. #TODO Robust logic 
  for node in allNodes:
    if node not in G.nodes:
      # Element has already been deleted so we do not need to consider it anymore
      continue
    if "nameless" not in node:
      childs = [c for c in G.successors(node)]
      parents = [p for p in G.predecessors(node)]
      toRemove.append(node)
      resultantEdgeCounter = 2**64 #There wont be graphs this large
      for parent in parents:
        for key in list(G.get_edge_data(parent, node).keys()):
          param = int(G.get_edge_data(parent, node, key)['sameVariableEdge'])
          G.remove_edge(parent, node)
          resultantEdgeCounter = min(edgeMap[(parent, node, key)], resultantEdgeCounter)
          del edgeMap[(parent, node, key)]
      for child in childs:
        for key in list(G.get_edge_data(node, child).keys()):
          param = int(G.get_edge_data(node, child, key)['sameVariableEdge'])
          G.remove_edge(node, child)
          resultantEdgeCounter = min(edgeMap[(node, child, key)], resultantEdgeCounter)
          del edgeMap[(node, child, key)]
      for child in childs:
        for parent in parents:
          param = len(G.get_edge_data(parent, child, default={}))
          G.add_edge(parent, child, sameVariableEdge = False)
          edgeMap[(parent, child, param)] = resultantEdgeCounter
  
  for node in toRemove:
    G.remove_node(node)


  def getXY(raw: Tuple[str, int]):
    return (positionStrToXcoord[raw[0]], raw[1])

  pos_raw = nx.get_node_attributes(G,'pos')
  pos = {}
  for key, value in pos_raw.items():
    pos[key] = getXY(value)

  for key, value in sorted(pos.items(), key=lambda item:item[1][1]):
    parentsYCoords = [pos[p][1] for p in G.predecessors(key)]
    if len(parentsYCoords) > 0:
      newYCoord = 1 + max(parentsYCoords)
    else:
      newYCoord = 0
    pos[key] = (pos[key][0], newYCoord)

  nodeNumber = 0
  nodeMap = {}
  nodeDetails = []
  edgeDetails = []
  for i, k in pos.items():
    nodeMap[i] = nodeNumber
    nodeNumber += 1
    nodeDetails.append([nodeNumber, -1, k[0]])
  for e in G.edges:
    edgeDetails.append([nodeMap[e[0]], nodeMap[e[1]], -1, 1.0])

  allNodeDetails.append(nodeDetails)
  allEdgeDetails.append(edgeDetails)
  a = nodeEdgeCounts[-1]
  nodeEdgeCounts.append((a[0] + len(nodeDetails), a[1] + len(edgeDetails)))

  printDebug(pos_raw)
  printDebug(pos)
  # nx.draw_networkx_nodes(G, pos)
  nx.draw_networkx_labels(G, pos, font_size=5)
  ax = plt.gca()
  # print(nx.get_edge_attributes(G,'isShadow'))
  plt.axis('off')
  plt.ion()
  plt.show()
  # print(G.edges)
  # print(G.nodes)
  # print(pos)
  for e in G.edges:
    printDebug(e)
  drawnNodes = set()
  plt.rcParams.update({'font.size': 5})

  for e in sorted(G.edges, key=lambda x: edgeMap[x]):
    plt.pause(0.005)
    nodes = [e[0], e[1]]
    for node in nodes:
      if node not in drawnNodes:
        plt.plot([pos[node][0]], [pos[node][1]], marker='o', color='g', label=node)
        drawnNodes.add(node)
    if nx.get_edge_attributes(G,'sameVariableEdge')[e] == False:      
      ax.annotate("",
          xy=pos[e[1]], xycoords='data',
          xytext=pos[e[0]], textcoords='data',
          arrowprops=dict(arrowstyle="->", color="0.1",
                  shrinkA=10, shrinkB=10,
                  patchA=None, patchB=None,
                  connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                  ),
                  ),
          )

  
  printDebug(sorted(allObservedPositions))
  # plt.show()
  generatedGraphs += 1
  print("Number of graphs generated: %d"%generatedGraphs)

  G = nx.MultiDiGraph()
  dependencyCount = 0
  allObservedPositions = set()
  variableToLatestVersion = {}
  object_id_to_heap_element_map = {}
  edgeCounter = 0
  edgeMap = {}

  return allNodeDetails, allEdgeDetails, nodeEdgeCounts