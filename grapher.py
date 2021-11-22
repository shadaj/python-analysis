# #WHAT I NEED TO DO
# MODEL THE BEHAVIOUR THAT INTERMEDIATE LIST ARE ALSO IN SOME ORDER CURRENTLY THAT BEHAVIOR IS LOST LEADING TO LOSS OF INTERMEDIATE INFORMATION 
# LOGICAL ADDRESSES OF INTERMEDIATES NEED TO BE KINDA SEMI CONCRETE

import networkx as nx
import matplotlib.pyplot as plt
import inspect
from collections import deque 

oneNodePerMemoryLocation = False


G = nx.MultiDiGraph()

numberOfContextAndVariable = 0
contextAndVariableToMemAddressMap = {}
baseVarToIndices = {}

variableMap = {}

functionCalls = 0
contextToIdMap = {}

halfDependencyQueue = deque()
joinedDependencies = []
callStackOffset = 0

def reduced_call_stack():
	# currentStack = inspect.stack()
	# #Remove first two frames which is functions inside grapher.py, and one more for current location of control in main program
	# reducedStack = tuple([(i.filename, i.lineno, i.function, i.index) for i in currentStack[callStackOffset+3:]])
	# # print(reducedStack)
	# return reducedStack
	return 123

def function_call():
	global functionCalls
	functionCalls += 1
	reducedStack = reduced_call_stack()
	if reducedStack in contextToIdMap:
		print("INFO: New context initialized")
	contextToIdMap[reducedStack] = functionCalls 


def produce_half_dependency(*halfDependencies):
	for halfDependency in halfDependencies:
		assert len(halfDependency) == 1, "Half Dependencies must be a singleton while producing"
		parent = halfDependency[0]

		try:
			localVariableContext = contextToIdMap[reduced_call_stack()]
		except:
			print(contextToIdMap)
			assert False, "Context not initialized"

		halfDependencyQueue.append((localVariableContext, parent))

def consume_half_dependency(*halfDependencies):
	global joinedDependencies, callStackOffset, baseVarToIndices, contextAndVariableToMemAddressMap
	for halfDependency in halfDependencies:
		assert len(halfDependency) == 1, "Half Dependencies must be a singleton while consuming"
		child = halfDependency[0]
		try:
			(parentContext, parent) = halfDependencyQueue.popleft()
		except:
			assert False, "No half dependency left to consume"

		try:
			childContext = contextToIdMap[reduced_call_stack()]
		except:
			print(contextToIdMap)
			assert False, "Context not initialized"

		# add_in_logical_memory(parentContext, parent, childContext, child)

		dependency = (child, parent)
		joinedDependencies.append(dependency)
		parentAddress = fetchOrCreateAddress(parentContext, parent, must_exist=True)
		# if (childContext, child[0]) not in baseVarToIndices:
		baseVarToIndices[(childContext, child[0])] = baseVarToIndices[(parentContext, parent[0])]
		for indices in baseVarToIndices[(childContext, child[0])]:
			flag = True
			# This thing is for multi dimensional arrays partially indexed
			for i, index in enumerate(child[1]):
				if indices[i] != index:
					flag=False
			if flag:
				contextAndVariableToMemAddressMap[(childContext, child[0], indices)] = contextAndVariableToMemAddressMap[(parentContext, parent[0], indices)]
		childAddress = fetchOrCreateAddress(childContext, child, must_exist=True)

	if len(halfDependencyQueue) == 0:
		callStackOffset += 1
		add_dependency_internal(parentContext, *joinedDependencies)
		callStackOffset -=1
		joinedDependencies = []

def fetchOrCreateAddress(contextID, variable, must_exist=False):
	global contextAndVariableToMemAddressMap, numberOfContextAndVariable, baseVarToIndices
	variableName = variable[0]
	variableIndices = [None]
	variableIndices.extend(list(variable[1]))
	iterIndices = []
	# print(variableIndices)
	for index in variableIndices:
		if index is not None:
			iterIndices.append(index)
		if (contextID, variableName, tuple(iterIndices)) in contextAndVariableToMemAddressMap:
			continue
		else:
			if (contextID, variableName) not in baseVarToIndices:
				baseVarToIndices[(contextID, variableName)] = []
			baseVarToIndices[(contextID, variableName)].append(tuple(iterIndices))
			if must_exist == True:
				assert False, "address should have already been assigned by now for " + str((contextID, variableName))
			numberOfContextAndVariable += 1
			contextAndVariableToMemAddressMap[(contextID, variableName, tuple(iterIndices))] = numberOfContextAndVariable
			print("New variable created: ", str((contextID, variableName, iterIndices)), " at memory address ", numberOfContextAndVariable)
	return contextAndVariableToMemAddressMap[(contextID, variableName, variable[1])]

def instantiate_variable(variable):
	global callStackOffset
	callStackOffset += 1
	instantiate_variable_internal(None, variable)
	callStackOffset -= 1

def instantiate_variable_internal(context, variable):
	global variableMap, contextToIdMap
	try:
		context = contextToIdMap[reduced_call_stack()]
	except:
		print(contextToIdMap)
		assert False, "Context not initialized. Is add_function() called within this function?"
	address = fetchOrCreateAddress(context, variable, must_exist=False)
	version = variableMap.get(address, (None, 0))[1]
	string = "l%d_v%d" % (address, version)
	G.add_node(string, pos=(address, version), rawLoc=str(variable))
	variableMap[address] = (string, version)

def add_dependency(*dependencies):
	print(dependencies)
	global callStackOffset
	callStackOffset += 1
	add_dependency_internal(None, *dependencies)
	callStackOffset -= 1

def add_dependency_internal(parentContext, *dependencies):
	dependencyToChildStrAndVersion = {}
	for dependency in dependencies:
		# print(dependency)
		assert len(dependency) == 2, "Dependencies must be in pairs only"
		child = dependency[0]
		parent = dependency[1]

		# print(child, parent)
		try:
			childContext = contextToIdMap[reduced_call_stack()]
			if parentContext is None:
				parentContext = childContext
		except:
			print(contextToIdMap)
			assert False, "Context not initialized. Is add_function() called within this function?"

		parentAddress = fetchOrCreateAddress(parentContext, parent, must_exist=True)
		childAddress = fetchOrCreateAddress(childContext, child, must_exist=False)
		
		# print(childAddress, childContext, child, parentAddress, parentContext, parent)

		
		childVersion = variableMap.get(childAddress, (None, 0))[1]
		parentVersion = variableMap.get(parentAddress, (None, 0))[1]
		
		oldChildVersion = childVersion
		childVersion = 0 if oneNodePerMemoryLocation and (not child.startswith('t')) else max(parentVersion, childVersion) + 1 

		childStr = "l%d_v%d" % (childAddress, childVersion)
		oldChildStr = variableMap.get(childAddress, (None, None))[0]
		parentStr = "l%d_v%d" % (parentAddress, parentVersion)
		
		dependencyToChildStrAndVersion[dependency] = (childStr, childVersion)
		G.add_node(parentStr, pos=(parentAddress, parentVersion), rawLoc=str(parent))
		G.add_node(childStr, pos=(childAddress, childVersion), rawLoc=str(child))
		
		G.add_edge(parentStr, childStr, isShadow=False)
		#Shadow edges ensure that Value (t+1) is plotted AFTER Value (t) always
		if oldChildStr is not None:
			G.add_edge(oldChildStr, childStr, isShadow=True)
		# input()

	for dependency in dependencies:
		child = dependency[0]

		try:
			childContext = contextToIdMap[reduced_call_stack()]
		except:
			print(contextToIdMap)
			assert False, "Context not initialized"

		childAddress = fetchOrCreateAddress(childContext, child)
		variableMap[childAddress] = dependencyToChildStrAndVersion[dependency] 


def showGraph(filterVar=None):
	global contextToIdMap
	# print(variableMap)
	# print(contextAndVariableToMemAddressMap)
	# print(baseVarToIndices)

	traversalQ = deque()

	# Only show nodes of those variables which are present in the output
	if filterVar is not None:
		context = contextToIdMap[reduced_call_stack()]
		currentVar = (context, filterVar)
		indices = baseVarToIndices[currentVar]

		# We know the graph is a DAG so no loops which simplifies the code
		listOfVisitedNodes = {}
		for index in indices:
			address = contextAndVariableToMemAddressMap[(context, filterVar, index)]
			node = variableMap[address][0]
			traversalQ.append(node)
			listOfVisitedNodes[node] = True

		while len(traversalQ) != 0:
			node = traversalQ.popleft()
			parentsOfNode = G.predecessors(node)
			for neighbor in parentsOfNode:
				if neighbor in listOfVisitedNodes:
					continue
				else:
					listOfVisitedNodes[neighbor] = True
					traversalQ.append(neighbor)

		nodesForRemoval = []
		for node in G.nodes:
			if node not in listOfVisitedNodes:
				nodesForRemoval.append(node)

		for node in nodesForRemoval:
			G.remove_node(node)



	print(len(nx.get_node_attributes(G, 'pos').keys()))
	print(len(nx.get_node_attributes(G, 'rawLoc').keys()))
	print(len(G.nodes))

	plt.subplot(121)
	
	foundIntermediate = True
	# Removing intermediate nodes
	# while foundIntermediate:
	# 	foundIntermediate = False
	# 	toRemove = []
	# 	for node in G.nodes:
	# 		# print(node, type(node))
	# 		if node.startswith('t'):
	# 			foundIntermediate = True
	# 			childs = G.successors(node)
	# 			parents = G.predecessors(node)
	# 			toRemove.append(node)
	# 			rawLocMap = nx.get_node_attributes(G, 'rawLoc')
	# 			for child in childs:
	# 				for parent in parents:
	# 					if rawLocMap[child] == rawLocMap[parent]:
	# 						G.add_edge(parent, child, isShadow=True)
	# 					G.add_edge(parent, child, isShadow=False)
	# 	for node in toRemove:
	# 		G.remove_node(node)

	# Adjusting height of all nodes
	orderOfNodes = {}

	print(len(nx.get_node_attributes(G, 'pos').keys()))
	print(len(nx.get_node_attributes(G, 'rawLoc').keys()))
	print(len(G.nodes))

	for node in G.nodes:
		if nx.get_node_attributes(G, 'pos')[node] not in orderOfNodes:
			orderOfNodes[nx.get_node_attributes(G, 'pos')[node]] = []
			orderOfNodes[nx.get_node_attributes(G, 'pos')[node]].append(node)
	for key in sorted(orderOfNodes, key=lambda x:(x[1], x[0])):
		# print(key)
		for node in orderOfNodes[key]:
			xcoord = nx.get_node_attributes(G, 'pos')[node][0]
			if len(list(G.predecessors(node))) > 0:
				# print(nx.get_node_attributes(G, 'pos')[node])
				# print([nx.get_node_attributes(G, 'pos')[i] for i in G.predecessors(node)])
				# print(node, [i for i in G.predecessors(node)])
				minHeight = max([nx.get_node_attributes(G, 'pos')[i][1] for i in G.predecessors(node)]) + 1
				nx.set_node_attributes(G, {node:{'pos':(xcoord,minHeight)}})
			else:
				nx.set_node_attributes(G, {node:{'pos':(xcoord,0)}})


	#Compress the graph to make it more clear. Just a heuristic, works well for sorting
	currentHeight = -1 #No node is given negative height
	counterForCurrentHeight = 0
	for key in sorted(orderOfNodes, key=lambda x:(x[1], x[0])):
		if key[1] > currentHeight:
			currentHeight = key[1]
			counterForCurrentHeight = 0
		for node in orderOfNodes[key]:
			# nx.set_node_attributes(G, {node:{'pos':(counterForCurrentHeight, currentHeight)}})
			counterForCurrentHeight += 1
			# print(counterForCurrentHeight, currentHeight)

	pos = nx.circular_layout(G) if oneNodePerMemoryLocation else nx.get_node_attributes(G,'pos')
	
	nx.draw_networkx_nodes(G, pos)
	nx.draw_networkx_labels(G, pos, font_size=5)
	ax = plt.gca()
	# print(nx.get_edge_attributes(G,'isShadow'))
	for e in G.edges:
		# print(e)
		if nx.get_edge_attributes(G,'isShadow')[e] == False:
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
	plt.savefig('graph.png', dpi=300)