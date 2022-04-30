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
random.seed(1)
receiver = DataTracingReceiver()

lower = 10
upper = 30

def testInsertionSort():
  global lower, upper
  from demos.insertsort import insertion_sort
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    insertion_sort(arr)
  print("InsertionSorted:", arr)

def testSelectionSort():
  global lower, upper
  from demos.selectsort import selection_sort
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    selection_sort(arr)
  print("SelectSorted:", arr)

def testMergeSort():
  global lower, upper
  from demos.mergesort import merge2
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    arr = merge2(arr)
  print("MergeSorted:", arr)

def testQuickSort():
  global lower, upper
  from demos.quicksort import quicksort_return
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    arr = quicksort_return(arr)
  print("QuickSorted:", arr)

def testBubbleSort():
  global lower, upper
  from demos.bubblesort import bubble, bubble_for
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    bubble_for(arr)
  print("BubbleSorted:", arr)

def testHeapSort():
  global lower, upper
  from demos.heapsort import heapsort
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    heapsort(arr)
  print("HeapSorted:", arr)

def testMatrixMultiplication():
  from demos.matmul import matmul_for, matmul_recursive, matmul_strassen, matmul2_for
  I = 2
  J = 2
  K = 2
  a = [[random.randint(0, 10) for i in range(J)] for j in range(I)]
  b = [[random.randint(0, 10) for i in range(K)] for j in range(J)]
  c = [[0 for i in range(K)] for j in range(I)]
  print(a, b, c)
  with receiver:
    c = matmul_strassen(a, b)
    # matmul_for(a, b, c)
    # matmul2_for(a, b, c)
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

def generateDataset(mode, num_datapoints):
  global receiver
  labels = [-1]
  import numpy as np
  from time import time
  def flatten(lol):
    return [i for l in lol for i in l]
  for i in range(num_datapoints):
    st = time()
    choice = random.randint(0,5)
    labels.append(choice)
    if choice == 0:
      testQuickSort()
    elif choice == 1:
      testHeapSort()
    elif choice == 2:
      testBubbleSort()
    elif choice == 3:
      testMergeSort()
    elif choice == 4:
      testInsertionSort()
    elif choice == 5:
      testSelectionSort()
    else:
      assert False, "Unexpected choice"
    en = time()
    print(en-st)
    _, times = receiver.receiverData
    print(times)
  (allNodeDetails, allEdgeDetails, nodeEdgeCounts), times = receiver.receiverData
  allNodeDetails = np.asarray(flatten(allNodeDetails))
  allEdgeDetails = np.asarray(flatten(allEdgeDetails))
  nodeEdgeCounts = np.concatenate([np.asarray(nodeEdgeCounts), np.expand_dims(np.asarray(labels), axis=1)], axis=1)

  np.save("/usr/local/lib/python3.9/site-packages/jraph/nodes%s.npy"%mode, allNodeDetails)
  np.save("/usr/local/lib/python3.9/site-packages/jraph/edges%s.npy"%mode, allEdgeDetails)
  np.save("/usr/local/lib/python3.9/site-packages/jraph/index%s.npy"%mode, nodeEdgeCounts)
  receiver.clear_cumulative_data()

# testMatrixMultiplication()
random.seed(1)
lower = 10
upper = 30
generateDataset("train", 10)
random.seed(5196)
lower = 10
upper = 30
generateDataset("test", 3)
random.seed(61295)
lower = 30
upper = 50
generateDataset("testL", 3)
random.seed(282)
lower = 50
upper = 100
generateDataset("testLL", 3)
# testMergeSort()
# testMatrixMultiplication()

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