from calendar import c
import math
from statistics import mean
from typing import Any, Dict, List, Set, Tuple, Union, Optional

from bytecode import Compare
import numpy as np

from .heap_object_tracking import HeapObjectTracker

from .data_tracing_variables import *

from .instrument import binary_ops, unary_ops

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque

from .helper import printDebug, isShowPlot

edgesSum = 0
nodesSum = 0

generatedGraphs = 0

def element_to_str(element: Union[SymbolicElement, StackElement], version: Optional[int] = None) -> str:
  if version is None:
    version = element.version
  return element.var_name + "#" + str(version)

def add_dependency_nonupdating(frameId: int, child: Union[SymbolicElement, StackElement], parent: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent: ", str(parent))
  add_dependency_internal(frameId, [(child, parent)])

def add_dependency(frameId: int, child: Union[SymbolicElement, StackElement], parent: Union[SymbolicElement, StackElement]) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent: ", str(parent))
  child.heap_elem = parent.heap_elem
  child.is_const = parent.is_const
  add_dependency_internal(frameId, [(child, parent)])

# def add_relation(value: bool, dest: Union[SymbolicElement, StackElement], orig: Union[SymbolicElement, StackElement], op: str) -> None:
#   global dependencyCount
#   dependencyCount += 1
#   printDebug("DEP COUNT: ", dependencyCount)
#   printDebug("New Relation (Dependency): ")
#   printDebug("Dest: ", str(dest))
#   printDebug("Origin: ", str(orig))
#   add_relation_internal(value, (dest, orig), op)

def add_dependency1(frameId: int, child: Union[SymbolicElement, StackElement], parent1: Union[SymbolicElement, StackElement], operation: Optional[str] = None) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent1: ", str(parent1))
  child.is_const = parent1.is_const
  add_dependency_internal(frameId, [(child, parent1)], operation)

def add_dependency2(frameId: int, child: Union[SymbolicElement, StackElement], parent1: Union[SymbolicElement, StackElement], parent2: Union[SymbolicElement, StackElement], operation: Optional[str] = None, establishedFact: Optional[Compare] = None) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  printDebug("Parent1: ", str(parent1))
  printDebug("Parent2: ", str(parent2))
  child.is_const = parent1.is_const and parent2.is_const
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
  child.is_const = parent1.is_const and parent2.is_const and parent3.is_const
  add_dependency_internal(frameId, [(child, parent1), (child, parent2), (child, parent3)])

def add_dependencyN(frameId: int, child: Union[SymbolicElement, StackElement], parents: List[Union[SymbolicElement, StackElement]], operation: Optional[str] = None) -> None:
  global dependencyCount
  dependencyCount += 1
  printDebug("DEP COUNT: ", dependencyCount)
  printDebug("New dependency: ")
  printDebug("Child: ", str(child))
  red = True
  depList = []
  for i, parent in enumerate(parents):
    printDebug("Parent%d: "%(i+1), str(parent))
    red = red and parent.is_const
    depList.append((child, parent))
  child.is_const = red
  add_dependency_internal(frameId, depList, operation)

allObservedPositions = set()
variableToLatestVersion = {}

current_heap_object_tracker: HeapObjectTracker = None

G = nx.MultiDiGraph()
dependencyCount = 0

allNodeDetails = []
allEdgeDetails = []
nodeEdgeCounts = [(0,0)]
edgeCounter = 0
edgeMap = {}

num_inputs = 0
inputs: Set[str] = set()
inputMap: Dict[str, Tuple[int, int, int]] = {}
num_outputs = 0
outputs: Set[str] = set()
outputMap: Dict[str, Tuple[int, int, int]] = {}

def set_current_heap_object_tracker(hot: HeapObjectTracker) -> None:
  global current_heap_object_tracker
  current_heap_object_tracker = hot

def bound_cnst(cnst) -> float:
  if not cnst == cnst:
    return 200.0
  if cnst == math.inf:
    return 100.0
  if cnst == -math.inf:
    return -100.0
  if cnst > 50 * math.pi:
    cnst = 50 * math.pi
  if cnst < -50 * math.pi:
    cnst = -50 * math.pi
  cnst = math.sin(cnst / 100) * 100
  return cnst

def get_const_number_instance(stack_or_heap_element: Union[SymbolicElement, StackElement]) -> Optional[Union[int, float]]:
  global current_heap_object_tracker
  if stack_or_heap_element.is_const:
    if isinstance(cnst := stack_or_heap_element.heap_elem.object_id, (bool, int)):
      return bound_cnst(cnst)
    elif isinstance(cnst := stack_or_heap_element.heap_elem.object_id, (str)):
      return None
    else:
      if isinstance(cnst2 := current_heap_object_tracker.get_by_id(cnst.id), (int, float)):
        return bound_cnst(cnst2)
      else:
        return None
  else:
    return None

def add_dependency_internal(frameId: int, depList: List[Tuple[Union[SymbolicElement, StackElement], Union[SymbolicElement, StackElement]]], operation: Optional[str] = None, establishedFact: Optional[Compare] = None) -> None:
  global allObservedPositions, edgeCounter, edgeMap
  if len(depList) == 2:
    assert depList[0][0] == depList[1][0], "Same child must be present in all dependencies"
  if len(depList) == 3:
    assert depList[0][0] == depList[1][0] == depList[2][0], "Same child must be present in all dependencies"

  child = depList[0][0]
  newChildVersion = 1 + max(max([dep[0].version for dep in depList]), max([dep[1].version for dep in depList]))
  child.version = newChildVersion
  childStr = element_to_str(child)

  oldChildVersion = variableToLatestVersion.get(child.var_name, None)
  variableToLatestVersion[child.var_name] = child.version

  isZero = False
  for dep in depList:
    parent = dep[1]
    parentStr = element_to_str(parent)
    cnst_val = get_const_number_instance(parent)
    if operation == "2*" and cnst_val == bound_cnst(0):
      isZero = True

  if isZero:
     G.add_node(childStr, pos=(child.var_name, child.version), frame = frameId, op = operation, fact = establishedFact, const_val = bound_cnst(0))
  else:
    if (cnst_val := get_const_number_instance(child)) is not None:
      G.add_node(childStr, pos=(child.var_name, child.version), frame = frameId, op = operation, fact = establishedFact, const_val = cnst_val)
    else:
      G.add_node(childStr, pos=(child.var_name, child.version), frame = frameId, op = operation, fact = establishedFact)

  if oldChildVersion is not None:
    oldChildStr = element_to_str(child, oldChildVersion)
    edgeCounter += 1
    param = len(G.get_edge_data(oldChildStr, childStr, default={}))
    edgeMap[(oldChildStr, childStr, param)] = edgeCounter
    G.add_edge(oldChildStr, childStr, sameVariableEdge = True)
    # assert nx.is_directed_acyclic_graph(G)

  allObservedPositions.add(child.var_name)

  for dep_i, dep in enumerate(depList):
    parent = dep[1]
    parentStr = element_to_str(parent)
    if parentStr == childStr:
      continue
    if parentStr not in G:
      if (cnst_val := get_const_number_instance(parent)) is not None:
        G.add_node(parentStr, pos=(parent.var_name, parent.version), frame = frameId, op = None, fact = None, const_val = cnst_val)
      else:
        G.add_node(parentStr, pos=(parent.var_name, parent.version), frame = frameId, op = None, fact = None)
    edgeCounter += 1
    param = len(G.get_edge_data(parentStr, childStr, default={}))
    edgeMap[(parentStr, childStr, param)] = edgeCounter
    cnst_val = get_const_number_instance(parent)
    if operation == "2+" and cnst_val == bound_cnst(0):
      pass
    elif operation == "2*" and (cnst_val == bound_cnst(1) or cnst_val == bound_cnst(0)):
      pass
    elif (operation == "2/" or operation == "2//") and cnst_val == bound_cnst(1) and dep_i == 1:
      pass
    elif operation == "2?" and (cnst_val == bound_cnst(math.inf) or cnst_val == bound_cnst(-math.inf)):
      pass
    else:
      G.add_edge(parentStr, childStr, sameVariableEdge = False)
    # assert nx.is_directed_acyclic_graph(G)

    variableToLatestVersion[parent.var_name] = parent.version

    allObservedPositions.add(parent.var_name)

def set_output(element: Union[StackElement, SymbolicElement]) -> None:
  global outputs, outputMap, num_outputs
  outputs.add(element_to_str(element))
  num_outputs += 1
  counter = 1
  outputMap[element_to_str(element)] = [2, num_outputs, counter]
  for i in element.heap_elem.collection_heap_elems:
    counter = set_output_internal(i, counter)
  outputMap[element_to_str(element)][2] /= counter
  outputMap[element_to_str(element)] = tuple(outputMap[element_to_str(element)])
  for i in element.heap_elem.collection_heap_elems:
    normalize_outputs(i, counter)

def set_output_internal(element: Union[StackElement, SymbolicElement], counter: int) -> int:
  global outputs, outputMap, num_outputs
  outputs.add(element_to_str(element))
  counter += 1
  outputMap[element_to_str(element)] = [2, num_outputs, counter]
  for i in element.heap_elem.collection_heap_elems:
    counter = set_output_internal(i, counter)
  return counter

def normalize_outputs(element: Union[StackElement, SymbolicElement], normalizer: int) -> None:
  global outputMap
  if not isinstance(outputMap[element_to_str(element)], tuple):
    outputMap[element_to_str(element)][2] /= normalizer
    outputMap[element_to_str(element)] = tuple(outputMap[element_to_str(element)])
  for i in element.heap_elem.collection_heap_elems:
    normalize_outputs(i, normalizer)

def set_input(element: Union[StackElement, SymbolicElement]) -> None:
  global inputs, inputMap, num_inputs
  inputs.add(element_to_str(element))
  num_inputs += 1
  counter = 1
  inputMap[element_to_str(element)] = [1, num_inputs, counter]
  for i in element.heap_elem.collection_heap_elems:
    counter = set_input_internal(i, counter)
  inputMap[element_to_str(element)][2] /= counter
  inputMap[element_to_str(element)] = tuple(inputMap[element_to_str(element)])
  for i in element.heap_elem.collection_heap_elems:
    normalize_inputs(i, counter)

def set_input_internal(element: Union[StackElement, SymbolicElement], counter: int) -> int:
  global inputs, inputMap, num_inputs
  inputs.add(element_to_str(element))
  counter += 1
  inputMap[element_to_str(element)] = [1, num_inputs, counter]
  for i in element.heap_elem.collection_heap_elems:
    counter = set_input_internal(i, counter)
  return counter

def normalize_inputs(element: Union[StackElement, SymbolicElement], normalizer: int) -> None:
  global inputMap
  inputMap[element_to_str(element)][2] /= normalizer
  inputMap[element_to_str(element)] = tuple(inputMap[element_to_str(element)])
  for i in element.heap_elem.collection_heap_elems:
    normalize_inputs(i, normalizer)

def is_input_or_output(nodeStr: str) -> bool:
  global inputs, outputs
  return nodeStr in inputs or nodeStr in outputs

def is_output(nodeStr: str) -> bool:
  global outputs
  return nodeStr in outputs

def is_input(nodeStr: str) -> bool:
  global inputs
  return nodeStr in inputs

def generate_memory_graph(trace_comparisions):
  global allObservedPositions, G, dependencyCount, variableToLatestVersion, generatedGraphs, object_id_to_heap_element_map, edgeMap, edgeCounter, inputs, outputs, inputMap, outputMap, num_inputs, num_outputs, edgesSum, nodesSum
  assert nx.is_directed_acyclic_graph(G)
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
    if is_input_or_output(node):
      relevantNodes.append(node)
    #if "nameless" in node: #and len([c for c in G.successors(node)]) == 0:
    #  relevantNodes.append(node)

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
  GnodeToConstVal = nx.get_node_attributes(G, 'const_val')

  # Pruning extra nodes. Any node which does not have "nameless" in it's name, i.e. is not a compound data structure (non primitive like int/str) 
  # is treated as a node to exclude. This is a temporary logic and can be changed in the future. #TODO Robust logic 
  from copy import deepcopy
  import numpy as np

  all_Nodes = list(reversed(list(nx.topological_sort(G))))

  
  def cleanGraph(stage):
    global edgeCounter
    nonlocal relevantNodes
    toRemove = []
    iteration = all_Nodes
    if stage == 2:
      iteration = list(reversed(iteration))
    for node in iteration:
      if node not in G.nodes:
        # Element has already been deleted so we do not need to consider it anymore
        continue
      if not is_input_or_output(node):
        childs = [c for c in G.successors(node)]
        parents = [p for p in G.predecessors(node)]
        childOp = [g for c in G.successors(node) if (g := GnodeToOp[c]) is not None]
        # childOp = []
        # parentOp = []
        operation = GnodeToOp[node]
        if operation is not None:
          op = operation[1:]
          arity = int(operation[0])
        else:
          op = None
          arity = None
        const = GnodeToConstVal.get(node, None)
        if stage == 1 or stage == 3:
          if ((operation is not None) or (const is not None and len(childOp) > 0)) and node in relevantNodes:
            continue
        elif stage == 2:
          if trace_comparisions:
            if not (operation is not None and len(parents) < arity):
              continue
          else:
            if op != "?":
              if not (operation is not None and len(parents) < arity):
                continue
        elif stage == 4:
          if op == "?":
            continue
          elif len(childs) != 0 or is_output(node):
            continue
        elif stage == 5:
          if node in relevantNodes:
            continue
        elif stage == 6:
          if not (op == "?" and len(childs) == 0): # We remove a ? node where there are no children
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
        parentsSameVariableEdge = []
        childsSameVariableEdge = []
        parentsDifferentVariableEdge = []
        childsDifferentVariableEdge = []
        for parent in parents:
          edge_data = deepcopy(G.get_edge_data(parent, node))
          for key in list(edge_data.keys()):
            param = int(edge_data[key]['sameVariableEdge'])
            if param:
              parentsSameVariableEdge.append(parent)
            else:
              parentsDifferentVariableEdge.append(parent)
            G.remove_edge(parent, node, key)
            resultantEdgeCounter = min(edgeMap[(parent, node, key)], resultantEdgeCounter)
            del edgeMap[(parent, node, key)]
        for child in childs:
          edge_data = deepcopy(G.get_edge_data(node, child))
          for key in list(edge_data.keys()):
            param = int(edge_data[key]['sameVariableEdge'])
            if param:
              childsSameVariableEdge.append(child)
            else:
              childsDifferentVariableEdge.append(child)
            G.remove_edge(node, child, key)
            resultantEdgeCounter = min(edgeMap[(node, child, key)], resultantEdgeCounter)
            del edgeMap[(node, child, key)]
        for child in childsDifferentVariableEdge: #childOp:
          for parent in parentsDifferentVariableEdge: #parentOp:
            param = len(G.get_edge_data(parent, child, default={}))
            G.add_edge(parent, child, sameVariableEdge = False)
            edgeMap[(parent, child, param)] = resultantEdgeCounter
        for child in childsSameVariableEdge:
          for parent in parentsSameVariableEdge:
            param = len(G.get_edge_data(parent, child, default={}))
            G.add_edge(parent, child, sameVariableEdge = True) 
            edgeMap[(parent, child, param)] = resultantEdgeCounter
    for node in toRemove:
      G.remove_node(node)

  printDebug(len(G.edges), len(G.nodes))

  cleanGraph(1)

  printDebug(len(G.edges), len(G.nodes))

  cleanGraph(2)

  printDebug(len(G.edges), len(G.nodes))

  cleanGraph(3)

  printDebug(len(G.edges), len(G.nodes))

  cleanGraph(4)

  printDebug(len(G.edges), len(G.nodes))

  printDebug(len(relevantNodes))
  
  relevantNodes = []
  for node in G.nodes:
    if is_input_or_output(node):
      relevantNodes.append(node)
    #if "nameless" in node: #and len([c for c in G.successors(node)]) == 0:
    #  relevantNodes.append(node)

  visitedQueue = deque(relevantNodes)
  relevantNodes = set()

  while len(visitedQueue) > 0:
    element = visitedQueue.popleft()
    relevantNodes.add(element)
    nbrs = [p for p in G.predecessors(element)] + [c for c in G.successors(element)]
    for nbr in nbrs:
      if nbr not in relevantNodes:
        visitedQueue.append(nbr)

  cleanGraph(5)

  printDebug(len(G.edges), len(G.nodes))

  edgesSum += len(G.edges)
  nodesSum += len(G.nodes)

  printDebug("!!!: ", edgesSum, ":::", nodesSum)

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

  relevantXcoords = 0
  oldXtoNewXcoords = {}
  for key, (oldX, _) in sorted(pos.items(), key = lambda item:item[1][0]):
    if is_input_or_output(key):
      if oldX not in oldXtoNewXcoords:
        oldXtoNewXcoords[oldX] = relevantXcoords
        relevantXcoords += 1


  for key, value in sorted(pos.items(), key = lambda item:item[1][1]):
    if not is_input_or_output(key):
      parentsXCoords = [pos[p][0] for p in G.predecessors(key)]
      if len(parentsXCoords) > 0:
        newXCoord = mean(parentsXCoords)
      else:
        newXCoord = relevantXcoords
        relevantXcoords += 1
      pos[key] = (newXCoord, value[1])
    else:
      pos[key] = (oldXtoNewXcoords[value[0]], value[1])

  printDebug(len(relevantNodes))

  cleanGraph(6)

  printDebug(len(G.edges), len(G.nodes))

  ops = {}
  for i, k in binary_ops.items():
    ops[i] = k
  for i, k in unary_ops.items():
    ops[i] = k

  opToId = {}
  for i, (k, v) in enumerate(ops.items()):
    opToId[v] = i + 1
  default_i = i + 2
  opToId[None] = 0

  # print(binary_ops)
  # print(unary_ops)
  # print(opToId)

  GsameVariableEdge = nx.get_edge_attributes(G,'sameVariableEdge')
  GfactEdge = {(u, v, k): d.get('fact',"") for u, v, k, d in G.edges(data=True, keys=True)}
  GfactContainingEdges = nx.get_edge_attributes(G, 'fact')
  GnodeToFrame = nx.get_node_attributes(G, 'frame')
  # GopEdge = {(u, v): d['op'] for u, v, d in G.edges(data=True)}

  nodeNumber = 0
  nodeMap = {}
  nodeDetails = []
  edgeDetails = []
  # low = min([k[0] for i, k in pos.items()])
  # high = max([k[0] for i, k in pos.items()])

  nodeToVector = {}
  for i, k in pos.items():
    constVal = GnodeToConstVal.get(i, None)
    nodeMap[i] = nodeNumber
    nodeNumber += 1
    if is_input(i):
      first_three = inputMap[i]
    elif is_output(i):
      first_three = outputMap[i]
    else:
      first_three = (0, 0, 0)
    if constVal is not None:
      consts = (1, float(constVal))
    else:
      consts = (0, 0)
    operation = opToId.get(GnodeToOp[i], default_i)
    nodeToVector[i] = (first_three + (operation,) + consts)
    nodeDetails.append([nodeMap[i], -1] + list(nodeToVector[i]))

  # for i, k in pos.items():
  #   nodeMap[i] = nodeNumber
  #   nodeNumber += 1
  #   nodeDetails.append([nodeNumber, -1, np.sin((k[0] - low) / (high - low)), opToId.get(GnodeToOp[i], default_i)])
    # nodeDetail = [nodeNumber, -1, I/O, -1, k[0]]
    # nodeDetails.append()
  for e in G.edges:
    val = int(GfactEdge[e])+1 if isinstance(GfactEdge[e], Compare) else 0
    edgeDetails.append([nodeMap[e[0]], nodeMap[e[1]], -1, val])

  allNodeDetails.append(nodeDetails)
  allEdgeDetails.append(edgeDetails)
  a = nodeEdgeCounts[-1]
  nodeEdgeCounts.append((a[0] + len(nodeDetails), a[1] + len(edgeDetails)))

  printDebug(pos_raw)
  printDebug(pos)

  if isShowPlot():
    GfactEdge = {(u, v): d.get('fact',"") for u, v, d in G.edges(data=True)}
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos, labels={n: \
      str(nodeToVector[n]) for n in G}, font_size=10)
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
    plt.pause(1)
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
  inputs = set()
  outputs = set()
  inputMap = {}
  outputMap = {}
  num_inputs = 0
  num_outputs = 0

  return allNodeDetails, allEdgeDetails, nodeEdgeCounts

def clear_cumulative_graph_data() -> None:
  global allNodeDetails, allEdgeDetails, nodeEdgeCounts, generatedGraphs
  allNodeDetails = []
  allEdgeDetails = []
  nodeEdgeCounts = [(0,0)]
  generatedGraphs = 0