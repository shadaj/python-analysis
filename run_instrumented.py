import imp
from re import L
from textwrap import dedent
from dis import opname

from instrumentation.stack_tracking_receiver import StackTrackingReceiver
from instrumentation.data_tracing_receiver import DataTracingReceiver
from instrumentation.module_loader import PatchingPathFinder
from instrumentation.exec import exec_instrumented

patcher = PatchingPathFinder()
patcher.install()

import random

receiver = DataTracingReceiver()

def testMergeSort():
  from demos.mergesort import merge2
  arr = [random.randint(0,10) for i in range(25)]
  print(arr)
  with receiver:
    arr = merge2(arr)
  print("MergeSorted:", arr)

def testQuickSort():
  from demos.quicksort import quicksort_return
  arr = [random.randint(0,10) for i in range(25)]
  print(arr)
  with receiver:
    arr = quicksort_return(arr)
  print("QuickSorted:", arr)

def testBubbleSort():
  from demos.bubblesort import bubble, bubble_for
  arr = [random.randint(0,10) for i in range(25)]
  print(arr)
  with receiver:
    arr = bubble_for(arr)
  print("BubbleSorted:", arr)

def testHeapSort():
  from demos.heapsort import heapsort
  arr = [random.randint(0,10) for i in range(25)]
  print(arr)
  with receiver:
    arr = heapsort(arr)
  print("HeapSorted:", arr)

def testMatrixMultiplication():
  from demos.matmul import matmul_for, matmul_recursive, matmul_strassen
  I = 4
  J = 4
  K = 4
  a = [[random.randint(0, 10) for i in range(J)] for j in range(I)]
  b = [[random.randint(0, 10) for i in range(K)] for j in range(J)]
  c = [[0 for i in range(K)] for j in range(I)]
  print(a, b, c)
  with receiver:
    c = matmul_strassen(a, b)
    # matmul_for(a, b, c)
    # c = matmul_recursive(a, b)
  print("Multiplication: ", a, b, c)

def testDp():
  from demos.dp import coinChange
  coins = [1,2,5]
  amount = 11
  with receiver:
    ans = coinChange(coins, amount)
  print("Coin change: ", coins, amount, ans)

def testTrial():
  from demos.simple import trial
  a = [1,2,3]
  with receiver:
    trial(a)


testMergeSort()

patcher.uninstall()

# allNodeDetails, allEdgeDetails, nodeEdgeCounts = receiver.receiverData
# import numpy as np

# def flatten(lol):
#   return [i for l in lol for i in l]

# allNodeDetails = np.asarray(flatten(allNodeDetails))
# allEdgeDetails = np.asarray(flatten(allEdgeDetails))
# nodeEdgeCounts = np.concatenate([np.asarray(nodeEdgeCounts), np.expand_dims(np.asarray(labels), axis=1)], axis=1)

# mode = "dump"

# np.save("/usr/local/lib/python3.9/site-packages/jraph/nodes%s.npy"%mode, allNodeDetails)
# np.save("/usr/local/lib/python3.9/site-packages/jraph/edges%s.npy"%mode, allEdgeDetails)
# np.save("/usr/local/lib/python3.9/site-packages/jraph/index%s.npy"%mode, nodeEdgeCounts)
# print("orig: " + str(orig_arr))
# print("out: " + str(arr))