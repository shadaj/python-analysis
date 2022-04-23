from statistics import mean
from typing import Any, Dict, List, Tuple, Union, Optional
from typing_extensions import Literal

from bytecode import Compare

from .heap_object_tracking import HeapObjectTracker

from .data_tracing_variables import *

import networkx as nx
import matplotlib.pyplot as plt

import copy
from collections import deque

from .helper import printDebug, isShowPlot

generatedGraphs = 0

def add_dependency(frameId: int, child: Union[SymbolicElement, StackElement], parent: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent: ", str(parent))
  child.heap_elem = parent.heap_elem
  add_dependency_internal(frameId, [(child, parent)])

# def add_relation(value: bool, dest: Union[SymbolicElement, StackElement], orig: Union[SymbolicElement, StackElement], op: str) -> None:
#   global dependencyCount
#   dependencyCount += 1
#   printDebug("DEP COUNT: ", dependencyCount)
#   printDebug("New Relation (Dependency): ")
#   printDebug("Dest: ", str(dest))
#   printDebug("Origin: ", str(orig))
#   add_relation_internal(value, (dest, orig), op)

def add_dependency2(frameId: int, child: Union[SymbolicElement, StackElement], parent1: Union[SymbolicElement, StackElement], parent2: Union[SymbolicElement, StackElement], operation: Optional[str] = None, establishedFact: Optional[Compare] = None) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent1: ", str(parent1))
  printDebug("Parent2: ", str(parent2))
  add_dependency_internal(frameId, [(child, parent1), (child, parent2)], operation, establishedFact)

def add_dependency3(frameId: int, child: Union[SymbolicElement, StackElement], parent1: Union[SymbolicElement, StackElement], parent2: Union[SymbolicElement, StackElement], parent3: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent1: ", str(parent1))
  printDebug("Parent2: ", str(parent2))
  printDebug("Parent3: ", str(parent3))
  add_dependency_internal(frameId, [(child, parent1), (child, parent2), (child, parent3)])

allObservedPositions = set()
variableToLatestVersion = {}

G = nx.MultiDiGraph()
dependencyCount = 0

allNodeDetails = []
allEdgeDetails = []
nodeEdgeCounts = [(0,0)]
edgeCounter = 0
edgeMap = {}

# def add_relation_internal(value: bool, depList: Tuple[Union[SymbolicElement, StackElement], Union[SymbolicElement, StackElement]], operation: str = "") -> None:
#   global edgeCounter, edgeMap
#   # No versioning checks required as no new nodes will be added. Only one edge between two eisting nodes will be added
#   edgeCounter += 1

#   child = depList[0]
#   childStr = child.var_name + "#" + str(child.version)

#   parent = depList[1]
#   parentStr = parent.var_name + "#" + str(parent.version)

#   param = len(G.get_edge_data(parentStr, childStr, default={}))
#   edgeMap[(parentStr, childStr, param)] = edgeCounter
#   label = ("true:" if value else "false:") + operation
#   G.add_edge(parentStr, childStr, sameVariableEdge = False, op = label)

def add_dependency_internal(frameId: int, depList: List[Tuple[Union[SymbolicElement, StackElement], Union[SymbolicElement, StackElement]]], operation: Optional[str] = None, establishedFact: Optional[Compare] = None) -> None:
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

  G.add_node(childStr, pos=(child.var_name, child.version), frame = frameId, op = operation, fact = establishedFact)

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
    if parentStr not in G:
      G.add_node(parentStr, pos=(parent.var_name, parent.version), frame = frameId, op = None, fact = None)
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
  
  if isShowPlot():
    plt.subplot(121)

  allNodes = [h for h in G.nodes]


  relevantNodes = []
  for node in allNodes:
    if "nameless" in node: #and len([c for c in G.successors(node)]) == 0:
      relevantNodes.append(node)

  visitedQueue = deque(relevantNodes)
  relevantNodes = set()

  while len(visitedQueue) > 0:
    element = visitedQueue.popleft()
    relevantNodes.add(element)
    nbrs = [p for p in G.predecessors(element)] + [c for c in G.successors(element)]
    for nbr in nbrs:
      if nbr not in relevantNodes:
        visitedQueue.append(nbr)

  GnodeToFrame = nx.get_node_attributes(G, 'frame')
  GnodeToOp = nx.get_node_attributes(G, 'op')
  GnodeToFact = nx.get_node_attributes(G, 'fact')

  # Pruning extra nodes. Any node which does not have "nameless" in it's name, i.e. is not a compound data structure (non primitive like int/str) 
  # is treated as a node to exclude. This is a temporary logic and can be changed in the future. #TODO Robust logic 
  from copy import deepcopy

  
  def cleanGraph(stage):
    global edgeCounter
    toRemove = []
    for node in allNodes:
      if node not in G.nodes:
        # Element has already been deleted so we do not need to consider it anymore
        continue
      if "nameless" not in node: #or GnodeToFrame[node] not in [0, 1, 10, 2, 5, 11, 14]:
        childs = [c for c in G.successors(node)]
        parents = [p for p in G.predecessors(node)]
        # childOp = []
        # parentOp = []
        
        if stage == 1:
          if GnodeToOp[node] is not None and node in relevantNodes:
            continue
        elif stage == 2:
          if GnodeToOp[node] != "?" or len(childs) > 0: # We remove a ? node where there are no children
            continue
          else:
            if len(parents) == 2:
              param = len(G.get_edge_data(parents[0],  parents[1], default={}))
              G.add_edge(parents[0], parents[1], fact = GnodeToFact[node], sameVariableEdge = False)
              edgeCounter += 1
              edgeMap[(parents[0], parents[1], param)] = edgeCounter
        else:
          raise NotImplementedError("Graph cleaning stage %d undefined" % stage)

        toRemove.append(node)
        resultantEdgeCounter = 2**64 #There wont be graphs this large
        parentsToIgnore = []
        childsToIgnore = []
        for parent in parents:
          edge_data = deepcopy(G.get_edge_data(parent, node))
          for key in list(edge_data.keys()):
            param = int(edge_data[key]['sameVariableEdge'])
            # op = edge_data[key]['op']
            if param:
              parentsToIgnore.append(parent)
            G.remove_edge(parent, node, key)
            resultantEdgeCounter = min(edgeMap[(parent, node, key)], resultantEdgeCounter)
            del edgeMap[(parent, node, key)]
            # parentOp.append((parent, op))
        for child in childs:
          edge_data = deepcopy(G.get_edge_data(node, child))
          for key in list(edge_data.keys()):
            param = int(edge_data[key]['sameVariableEdge'])
            # op = edge_data[key]['op']
            if param:
              childsToIgnore.append(child)
            G.remove_edge(node, child, key)
            resultantEdgeCounter = min(edgeMap[(node, child, key)], resultantEdgeCounter)
            del edgeMap[(node, child, key)]
            # childOp.append((child, op))
        for child in childs: #childOp:
          if child in childsToIgnore:
            continue
          for parent in parents:#parentOp:
            if parent in parentsToIgnore:
              continue
            # op = op1 + op2 #Only one of op1, op2 are can be nontrivial (non "")
            param = len(G.get_edge_data(parent, child, default={}))
            G.add_edge(parent, child, sameVariableEdge = False)
            edgeMap[(parent, child, param)] = resultantEdgeCounter
        for child in childsToIgnore:
          for parent in parentsToIgnore:
            param = len(G.get_edge_data(parent, child, default={}))
            G.add_edge(parent, child, sameVariableEdge = True) 
            edgeMap[(parent, child, param)] = resultantEdgeCounter
    for node in toRemove:
      G.remove_node(node)

  
  cleanGraph(1)

  print(len(G.edges), len(G.nodes))

  def getXY(raw: Tuple[str, int]):
    return (positionStrToXcoord[raw[0]], raw[1])

  # Convert Variable names into X-Y coordinates
  pos_raw = nx.get_node_attributes(G,'pos')
  pos = {}
  for key, value in pos_raw.items():
    pos[key] = getXY(value)

  # Reduce the Y-Coordinate to make the graph pretty
  for key, value in sorted(pos.items(), key=lambda item:item[1][1]):
    parentsYCoords = [pos[p][1] for p in G.predecessors(key)]
    if len(parentsYCoords) > 0:
      newYCoord = 1 + max(parentsYCoords)
    else:
      newYCoord = 0
    pos[key] = (pos[key][0], newYCoord)

  namelessXcoords = 0
  for key, _ in sorted(pos.items(), key = lambda item:item[1][1]):
    if "nameless" in key:
      namelessXcoords = max(namelessXcoords, pos[key][0])

  for key, value in sorted(pos.items(), key = lambda item:item[1][1]):
    if "nameless" not in key:
      parentsXCoords = [pos[p][0] for p in G.predecessors(key)]
      if len(parentsXCoords) > 0:
        newXCoord = mean(parentsXCoords)
      else:
        newXCoord = namelessXcoords
        namelessXcoords += 1
      pos[key] = (newXCoord, pos[key][1])

  cleanGraph(2)

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

  GsameVariableEdge = nx.get_edge_attributes(G,'sameVariableEdge')
  GfactEdge = {(u, v): d.get('fact',"") for u, v, d in G.edges(data=True)}
  GfactContainingEdges = nx.get_edge_attributes(G, 'fact')
  GnodeToFrame = nx.get_node_attributes(G, 'frame')
  # GopEdge = {(u, v): d['op'] for u, v, d in G.edges(data=True)}

  if isShowPlot():
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos, labels={n: \
      str(GnodeToFrame[n]) + ":" + str(GnodeToOp[n] if GnodeToOp[n] is not None else "") \
         for n in G}, font_size=10)
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=GopEdge, font_size=10, bbox=dict(alpha=0))
    nx.draw_networkx_edge_labels(G, pos, edge_labels=GfactEdge, font_size=10, bbox=dict(alpha=0))

  if isShowPlot():
    ax = plt.gca()
    plt.axis('off')

  # print(nx.get_edge_attributes(G,'isShadow'))
  # plt.ion()
  # plt.show()
  # print(G.edges)
  # print(G.nodes)
  # print(pos)
  for e in G.edges:
    printDebug(e)
  drawnNodes = set()

  if isShowPlot():
    plt.rcParams.update({'font.size': 5})

  # fig = plt.figure()
  # ax = fig.add_subplot(111)

  # minX, maxX = 2**64, -2**64
  # minY, maxY = 2**64, -2**64
  # for _, (x, y) in pos.items():
  #   minX = min(minX, x)
  #   maxX = max(maxX, x)
  #   minY = min(minY, y)
  #   maxY = max(maxY, y)

  # x, y = [], []
  # line1, = ax.plot(x,y,'g*')

  # ax.set_xlim([minX-10, maxX+10])
  # ax.set_ylim([minY-1, maxY+1])


  for e in sorted(G.edges, key=lambda x: edgeMap[x]):
  #   st = time()
  #   plt.pause(0.005)
  #   nodes = [e[0], e[1]]
  #   for node in nodes:
  #     if node not in drawnNodes:
  #       x.append(pos[node][0])
  #       y.append(pos[node][1])
  #       drawnNodes.add(node)
  #       line1.set_ydata(y)
  #       line1.set_xdata(x)
  #   if attributeGraph[e] == False:
  #     x_, y_ = pos[e[0]]
  #     xdx, ydy = pos[e[1]]
  #     dx, dy = xdx - x_, ydy - y_
  #     # ret = ax.arrow(x_, y_, dx, dy, animated=True)
  #     # print(ret)
  #     # input()
  #     # ax.draw_artist(ret)
  #   fig.canvas.draw()
  #   fig.canvas.flush_events()
  #   # input()
  #   en = time()
  #   # if attributeGraph[e] == False:
      
  #   # if attributeGraph[e] == False:      
  #   #   ax.annotate("",
  #   #       xy=pos[e[1]], xycoords='data',
  #   #       xytext=pos[e[0]], textcoords='data',
  #   #       arrowprops=dict(arrowstyle="->", color="0.1",
  #   #               shrinkA=10, shrinkB=10,
  #   #               patchA=None, patchB=None,
  #   #               connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
  #   #               ),
  #   #               ),
  #   #       )
  #   print(en - st)
    # nodes = [e[0], e[1]]
    # for node in nodes:
    #   if node not in drawnNodes:
    #     plt.plot([pos[node][0]], [pos[node][1]], marker='o', color='g', label=node)
    #     drawnNodes.add(node)
    if GsameVariableEdge[e] == False:    
      if isShowPlot():  
        ax.annotate("",
          xy=pos[e[1]], xycoords='data',
          xytext=pos[e[0]], textcoords='data',
          arrowprops=dict(arrowstyle="->", color="0.1" if e not in GfactContainingEdges else "0.7",
                  shrinkA=10, shrinkB=10,
                  patchA=None, patchB=None,
                  connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
                  ),
                  ),
          )
        # labelLoc = ((pos[e[0]][0] + pos[e[1]][0]) / 2, (pos[e[0]][1] + pos[e[1]][1]) / 2)
        # ax.annotate(GopEdge[e], xy = labelLoc, xycoords='data', xytext = labelLoc, textcoords='data', arrowprops=dict(arrowstyle="->", color="0.1",
        #           shrinkA=10, shrinkB=10,
        #           patchA=None, patchB=None,
        #           connectionstyle="arc3,rad=rrr".replace('rrr',str(0.3*e[2])
        #           ),
        #           ),)


  
  printDebug(sorted(allObservedPositions))
  if isShowPlot():
    plt.show()
  generatedGraphs += 1
  print("Number of graphs generated: %d"%generatedGraphs)

  G = nx.MultiDiGraph()
  dependencyCount = 0
  allObservedPositions = set()
  variableToLatestVersion = {}
  object_id_to_heap_element_map.clear()
  edgeCounter = 0
  edgeMap = {}

  return allNodeDetails, allEdgeDetails, nodeEdgeCounts