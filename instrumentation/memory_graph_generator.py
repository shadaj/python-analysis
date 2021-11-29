from typing import Any, Dict, List, Tuple, Union, Optional
from typing_extensions import Literal

from .heap_object_tracking import HeapObjectTracker

from .data_tracing_variables import *

import networkx as nx
import matplotlib.pyplot as plt

import copy

G = nx.MultiDiGraph()


dependencyCount = 0

def add_dependency(child: Union[SymbolicElement, StackElement], parent: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  print("DEP COUNT: ", dependencyCount)
  print("New dependency: ")
  print("Child: ", str(child))
  print("Parent: ", str(parent))
  child.heap_elem = parent.heap_elem
  add_dependency_internal([(child, parent)])

def add_dependency2(child: Union[SymbolicElement, StackElement], parent1: Union[SymbolicElement, StackElement], parent2: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  print("DEP COUNT: ", dependencyCount)
  print("New dependency: ")
  print("Child: ", str(child))
  print("Parent1: ", str(parent1))
  print("Parent2: ", str(parent2))
  add_dependency_internal([(child, parent1), (child, parent2)])

allObservedPositions = set()
variableToLatestVersion = {}

def add_dependency_internal(depList: List[Tuple[Union[SymbolicElement, StackElement], Union[SymbolicElement, StackElement]]]) -> None:
  global allObservedPositions
  if len(depList) == 2:
    assert depList[0][0] == depList[1][0], "Same child must be present in all dependencies"
  
  child = depList[0][0]
  newChildVersion = 1 + max(max([dep[0].version for dep in depList]), max([dep[1].version for dep in depList]))
  child.version = newChildVersion
  childStr = child.var_name + "#" + str(child.version)

  oldChildVersion = variableToLatestVersion.get(child.var_name, None)
  variableToLatestVersion[child.var_name] = child.version

  G.add_node(childStr, pos=(child.var_name, child.version))

  if oldChildVersion is not None:
    oldChildStr = child.var_name + "#" + str(oldChildVersion)
    G.add_edge(oldChildStr, childStr, sameVariableEdge = True)

  allObservedPositions.add(child.var_name)

  for dep in depList:
    parent = dep[1]
    parentStr = parent.var_name + "#" + str(parent.version)

    G.add_node(parentStr, pos=(parent.var_name, parent.version))
    G.add_edge(parentStr, childStr, sameVariableEdge = False)

    variableToLatestVersion[parent.var_name] = parent.version

    allObservedPositions.add(parent.var_name)

def generate_memory_graph():
  global allObservedPositions
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
    if False: #"nameless" not in node:
      childs = [c for c in G.successors(node)]
      parents = [p for p in G.predecessors(node)]
      toRemove.append(node)
      for parent in parents:
        G.remove_edge(parent, node)
      for child in childs:
        G.remove_edge(node, child)
      for child in childs:
        for parent in parents:
          G.add_edge(parent, child, sameVariableEdge = False)
  
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

  print(pos_raw)
  print(pos)
  nx.draw_networkx_nodes(G, pos)
  nx.draw_networkx_labels(G, pos, font_size=5)
  ax = plt.gca()
  # print(nx.get_edge_attributes(G,'isShadow'))
  for e in G.edges:
    print(e)
  for e in G.edges:
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
  plt.axis('off')
  plt.show()

  print(sorted(allObservedPositions))