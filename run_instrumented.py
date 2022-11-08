import os
from re import L
from textwrap import dedent
from dis import opname

import sys
from numpy import dtype

from instrumentation.stack_tracking_receiver import StackTrackingReceiver
from instrumentation.data_tracing_receiver import DataTracingReceiver
from instrumentation.module_loader import PatchingPathFinder
from instrumentation.exec import exec_instrumented
from instrumentation.predict import evaluate, get_graph_test

import sys
sys.path.append("/home/aayan/Desktop/Research")
sys.path.append("/Users/aayan/Desktop/Research")

patcher = PatchingPathFinder()
patcher.install()

import random
# random.seed(1)
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
    arr = insertion_sort(arr)
  print("InsertionSorted:", arr)

def testSelectionSort():
  global lower, upper
  from demos.selectsort import selection_sort
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    arr = selection_sort(arr)
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

def testArgMergeSort():
  global lower, upper
  from demos.mergesort import argmerge
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    indices = argmerge(arr)
  print("MergeSorted:", indices)

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
    arr = bubble_for(arr)
  print("BubbleSorted:", arr)

def testHeapSort():
  global lower, upper
  from demos.heapsort import heapsort
  l = random.randint(lower, upper)
  arr = [random.randint(0,10) for i in range(l)]
  print(arr)
  with receiver:
    arr = heapsort(arr)
  print("HeapSorted:", arr)

def testMatrixMultiplication():
  from demos.matmul import matmul_for, matmul_recursive, matmul_strassen, matmul2_for
  I = 4
  J = 4
  K = 4
  a = [[random.randint(0, 10) for i in range(J)] for j in range(I)]
  b = [[random.randint(0, 10) for i in range(K)] for j in range(J)]
  c = [[0 for i in range(K)] for j in range(I)]
  print(a, b, c)
  with receiver:
    # c = matmul_strassen(a, b)
    c = matmul_for(a, b, c)
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


####################################################################################################################################
############################################ NUMPY APIs ############################################################################
####################################################################################################################################

### HELPER

def get_broadcast_compatible_shape(original, max_dim):
  import numpy as np
  if np.random.randint(0, 2):
    return original
  new_shape = []
  for i in original[::-1]:
    if i == 1:
      if np.random.randint(0, 2):
        new_shape.append(np.random.randint(2, max_dim + 1))
      else:
        new_shape.append(i)
    else:
      if np.random.randint(0, 2):
        new_shape.append(1)
      else:
        new_shape.append(i)
    if np.random.randint(0, 2):
      return new_shape[::-1]
  if np.random.randint(0, 2):
    new_shape.append(np.random.randint(1, max_dim + 1))
  return new_shape[::-1]


### DATASET GENERATORS

def testReductionSum(dims, dim_size_max):
  import numpy as np
  import APIs.sum as sum
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_where = get_broadcast_compatible_shape(size, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size), size=np.random.choice(len(size)), replace=False).tolist()]) 
  keepdims = np.random.choice([None, True])
  initial = np.random.choice([None, 1])
  where = np.random.choice([None, np.random.choice([True, False], size=size_where).tolist()])
  print(a, size)
  print(axis)
  print(keepdims)
  print(initial)
  print(where, size_where)
  with receiver:
    ans = sum.sum_1(a, axis=axis, keepdims=keepdims, initial=initial, where=where)
  print("reduction sum: ", ans)

def testReductionProd(dims, dim_size_max):
  import numpy as np
  import APIs.prod as prod
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_where = get_broadcast_compatible_shape(size, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size), size=np.random.choice(len(size)), replace=False).tolist()]) 
  keepdims = np.random.choice([None, True])
  initial = np.random.choice([None, 1])
  where = np.random.choice([None, np.random.choice([True, False], size=size_where).tolist()])
  print(a, size)
  print(axis)
  print(keepdims)
  print(initial)
  print(where, size_where)
  with receiver:
    ans = prod.prod_1(a, axis=axis, keepdims=keepdims, initial=initial, where=where)
  print("reduction prod: ", ans)

def testReductionMax(dims, dim_size_max):
  import numpy as np
  import APIs.max as max
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_where = get_broadcast_compatible_shape(size, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size), size=np.random.choice(len(size)), replace=False).tolist()]) 
  keepdims = np.random.choice([None, True])
  initial = np.random.choice([None, 1])
  where = np.random.choice([None, np.random.choice([True, False], size=size_where).tolist()])
  print(a, size)
  print(axis)
  print(keepdims)
  print(initial)
  print(where, size_where)
  with receiver:
    ans = max.max_1(a, axis=axis, keepdims=keepdims, initial=initial, where=where)
  print("reduction max: ", ans)

def testReductionMin(dims, dim_size_max):
  import numpy as np
  import APIs.min as min
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_where = get_broadcast_compatible_shape(size, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size), size=np.random.choice(len(size)), replace=False).tolist()]) 
  keepdims = np.random.choice([None, True])
  initial = np.random.choice([None, 1])
  where = np.random.choice([None, np.random.choice([True, False], size=size_where).tolist()])
  print(a, size)
  print(axis)
  print(keepdims)
  print(initial)
  print(where, size_where)
  with receiver:
    ans = min.min_1(a, axis=axis, keepdims=keepdims, initial=initial, where=where)
  print("reduction min: ", ans)

def testReductionMean(dims, dim_size_max):
  import numpy as np
  import APIs.mean as mean
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_where = get_broadcast_compatible_shape(size, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size), size=np.random.choice(len(size)), replace=False).tolist()]) 
  keepdims = np.random.choice([None, True])
  where = np.random.choice([None, np.random.choice([True, False], size=size_where).tolist()])
  print(a, size)
  print(axis)
  print(keepdims)
  print(where, size_where)
  with receiver:
    ans = mean.mean_1(a, axis=axis, keepdims=keepdims, where=where)
  print("reduction min: ", ans)

def testReductionAll(dims, dim_size_max):
  import numpy as np
  import APIs.all as all
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_where = get_broadcast_compatible_shape(size, dim_size_max)
  a = np.random.choice([True, False], size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size), size=np.random.choice(len(size)), replace=False).tolist()]) 
  keepdims = np.random.choice([None, True])
  where = np.random.choice([None, np.random.choice([True, False], size=size_where).tolist()])
  print(a, size)
  print(axis)
  print(keepdims)
  print(where, size_where)
  with receiver:
    ans = all.all_1(a, axis=axis, keepdims=keepdims, where=where)
  print("reduction all: ", ans)

def testReductionAny(dims, dim_size_max):
  import numpy as np
  import APIs.any as any
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_where = get_broadcast_compatible_shape(size, dim_size_max)
  a = np.random.choice([True, False], size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size), size=np.random.choice(len(size)), replace=False).tolist()]) 
  keepdims = np.random.choice([None, True])
  where = np.random.choice([None, np.random.choice([True, False], size=size_where).tolist()])
  print(a, size)
  print(axis)
  print(keepdims)
  print(where, size_where)
  with receiver:
    ans = any.any_1(a, axis=axis, keepdims=keepdims, where=where)
  print("reduction any: ", ans)

def testAdd(dims, dim_size_max):
  import numpy as np
  import APIs.add as add
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = get_broadcast_compatible_shape(size_a, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = add.add_1(a, b)
  print("add: ", ans)

def testSubtract(dims, dim_size_max):
  import numpy as np
  import APIs.sub as sub
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = get_broadcast_compatible_shape(size_a, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = sub.sub_1(a, b)
  print("sub: ", ans)

def testDivide(dims, dim_size_max):
  import numpy as np
  import APIs.div as div
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = get_broadcast_compatible_shape(size_a, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.randint(-5, 5, size=size_b).tolist()
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = div.div_1(a, b)
  print("div: ", ans)

def testMultiply(dims, dim_size_max):
  import numpy as np
  import APIs.mul as mul
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = get_broadcast_compatible_shape(size_a, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = mul.mul_1(a, b)
  print("mul: ", ans)

def testPower(dims, dim_size_max):
  import numpy as np
  import APIs.pow as pow
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = get_broadcast_compatible_shape(size_a, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = pow.pow_1(a, b)
  print("pow: ", ans)

def testAbs(dims, dim_size_max):
  import numpy as np
  import APIs.abs as abs
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  print(a, size_a)
  with receiver:
    ans = abs.abs_1(a)
  print("abs: ", ans)

def testExp(dims, dim_size_max):
  import numpy as np
  import APIs.exp as exp
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  print(a, size_a)
  with receiver:
    ans = exp.exp_1(a)
  print("pow: ", ans)

def testSqrt(dims, dim_size_max):
  import numpy as np
  import APIs.sqrt as sqrt
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  print(a, size_a)
  with receiver:
    ans = sqrt.sqrt_1(a)
  print("sqrt: ", ans)

def testZeros(dims, dim_size_max):
  import numpy as np
  import APIs.zeros as zeros
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  print(size)
  with receiver:
    ans = zeros.zeros_1(size)
  print("zeros: ", ans)

def testZerosLike(dims, dim_size_max):
  import numpy as np
  import APIs.zeros_like as zeros_like
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  print(a, size)
  with receiver:
    ans = zeros_like.zeros_like_1(a)
  print("zeros like: ", ans)

def testOnes(dims, dim_size_max):
  import numpy as np
  import APIs.ones as ones
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  print(size)
  with receiver:
    ans = ones.ones_1(size)
  print("ones: ", ans)

def testOnesLike(dims, dim_size_max):
  import numpy as np
  import APIs.ones_like as ones_like
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  print(a, size)
  with receiver:
    ans = ones_like.ones_like_1(a)
  print("ones like: ", ans)

def testShape(dims, dim_size_max):
  import numpy as np
  import APIs.shape as shape
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  print(a, size)
  with receiver:
    ans = shape.shape_1(a)
  print("shape: ", ans)

def testTranspose(dims, dim_size_max):
  import numpy as np
  import APIs.transpose as transpose
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  axis = np.random.choice([None, np.random.permutation(len(size)).tolist()])
  print(a, size)
  print(axis)
  with receiver:
    ans = transpose.transpose_1(a, axis)
  print("transpose: ", ans)

def testEye(dims, dim_size_max):
  import numpy as np
  import APIs.eye as eye
  N = np.random.randint(1, dim_size_max+1)
  M = np.random.choice([None, np.random.randint(1, dim_size_max+1)])
  mx = max(N, M) if M is not None else N
  k = np.random.choice([0, np.random.randint(-mx, mx+1)]).item() # Weird typecasting being done by np.random.choice
  print(N)
  print(M)
  print(k)
  with receiver:
    ans = eye.eye_1(N, M, k)
  print("eye: ", ans)

def testConcatenate(dims, dim_size_max):
  import numpy as np
  import APIs.concatenate as concatenate
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  axis = np.random.choice([None, np.random.randint(len(size))])
  N = np.random.randint(1, dims+1) # Number of arrays to concatenate, using dims variable
  arrays = []
  print(axis)
  for i in range(N):
    if axis is not None:
      size_ = list(size)
      size_[axis] = np.random.randint(1, dim_size_max+1) # Concatenated axis may be different in all operands
    else:
      size_ = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
    a = np.random.uniform(low=-10., high=10., size=size_).tolist()
    print(a, size_)
    arrays.append(a)
  with receiver:
    ans = concatenate.concatenate_1(axis, *arrays)
  print("concatenate: ", ans)

def testDot(dims, dim_size_max):
  import numpy as np
  import APIs.dot as dot
  size_a = ([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = ([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  if len(size_b) == 1:
    size_b[-1] = size_a[-1]
  elif len(size_b) >= 2:
    size_b[-2] = size_a[-1]
  size_a = tuple(size_a)
  size_b = tuple(size_b)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = dot.dot_1(a, b)
  print("dot: ", ans)

def testArange(dims, dim_size_max):
  import numpy as np
  import APIs.arange as arange
  start = np.random.randint(dim_size_max * 20)
  stop = np.random.choice([None, np.random.randint(dim_size_max * 10)])
  stop = stop + start if stop is not None else None
  step = np.random.choice([None] + [i for i in range(1, dim_size_max)] + [i for i in range(-dim_size_max, 0)])
  print(start)
  print(stop)
  print(step)
  with receiver:
    ans = arange.arange_1(start, stop, step)
  print("arange: ", ans)


def testLinspace(dims, dim_size_max):
  import numpy as np
  import APIs.linspace as linspace
  size_start = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_stop = get_broadcast_compatible_shape(size_start, dim_size_max)
  start = np.random.uniform(low=-10., high=10., size=size_start).tolist()
  stop = np.random.uniform(low=-10., high=10., size=size_stop).tolist()
  num = np.random.choice([2, 3, dim_size_max])
  endpoint = np.random.choice([True, False])
  retstep = np.random.choice([True, False])
  axis = np.random.choice([np.random.randint(len(size_start))])
  print(start)
  print(stop)
  print(num)
  print(endpoint)
  print(retstep)
  print(axis)
  with receiver:
    ans = linspace.linspace_1(start, stop, num, endpoint, retstep, axis)
  print("linspace: ", ans)


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
#random.seed(1)
#lower = 10
#upper = 30
#generateDataset("train", 10000)
#random.seed(5196)
#lower = 10
#upper = 30
#generateDataset("test", 3000)
#random.seed(61295)
#lower = 30
#upper = 50
#generateDataset("testL", 3000)
#random.seed(282)
#lower = 50
#upper = 100
#generateDataset("testLL", 500)
# random.seed(1906)
# lower = 200
# upper = 500
# generateDataset("testLLLL", 500)
# testReductionSum()
# testMatrixMultiplication()

IntToClassMapping = {
  0: "Sum",
  1: "Prod",
  2: "Max",
  3: "Min",
  4: "Mean",
  5: "All",
  6: "Any",
  7: "Add",
  8: "Subtract",
  9: "Multiply",
  10: "Divide",
  11: "Power",
  12: "Abs",
  13: "Exp",
  14: "Sqrt",
  15: "Zeros",
  16: "ZerosLike",
  17: "Ones",
  18: "OnesLike",
  19: "Shape",
  20: "Transpose",
  21: "Eye",
  22: "Concatenate",
  23: "Dot",
  24: "Linspace",
  25: "Arange",
}

def generateDataset(mode, num_datapoints, instance_id):
  global receiver
  labels = [-1]
  import numpy as np
  from time import time
  def flatten(lol):
    return [i for l in lol for i in l]
  def get_sizes(mode, choice):
    if mode == "train":
      if choice >= 24:
        return (2, 2)
      else:
        return (2, 6)
    elif mode == "test":
      if choice >= 24:
        return (2, 2)
      else:
        return (2, 6)
    elif mode == "testL":
      if choice >= 24:
        return (3, 3)
      else:
        return (3, 7)
    elif mode == "testLL":
      if choice >= 24:
        return (3, 4)
      else:
        return (3, 10)
    elif mode == "testLLL":
      if choice >= 24:
        return (3, 5)
      else:
        return (3, 20)
  for i in range(num_datapoints):
    st = time()
    choice = random.randint(0,25)
    labels.append(choice)
    if choice == 0:
      testReductionSum(*get_sizes(mode, choice))
    elif choice == 1:
      testReductionProd(*get_sizes(mode, choice))
    elif choice == 2:
      testReductionMax(*get_sizes(mode, choice))
    elif choice == 3:
      testReductionMin(*get_sizes(mode, choice))
    elif choice == 4:
      testReductionMean(*get_sizes(mode, choice))
    elif choice == 5:
      testReductionAll(*get_sizes(mode, choice))
    elif choice == 6:
      testReductionAny(*get_sizes(mode, choice))
    elif choice == 7:
      testAdd(*get_sizes(mode, choice))
    elif choice == 8:
      testSubtract(*get_sizes(mode, choice))
    elif choice == 9:
      testMultiply(*get_sizes(mode, choice))
    elif choice == 10:
      testDivide(*get_sizes(mode, choice))
    elif choice == 11:
      testPower(*get_sizes(mode, choice))
    elif choice == 12:
      testAbs(*get_sizes(mode, choice))
    elif choice == 13:
      testExp(*get_sizes(mode, choice))
    elif choice == 14:
      testSqrt(*get_sizes(mode, choice))
    elif choice == 15:
      testZeros(*get_sizes(mode, choice))
    elif choice == 16:
      testZerosLike(*get_sizes(mode, choice))
    elif choice == 17:
      testOnes(*get_sizes(mode, choice))
    elif choice == 18:
      testOnesLike(*get_sizes(mode, choice))
    elif choice == 19:
      testShape(*get_sizes(mode, choice))
    elif choice == 20:
      testTranspose(*get_sizes(mode, choice))
    elif choice == 21:
      testEye(*get_sizes(mode, choice))
    elif choice == 22:
      testConcatenate(*get_sizes(mode, choice))
    elif choice == 23:
      testDot(*get_sizes(mode, choice))
    elif choice == 24:
      testLinspace(*get_sizes(mode, choice))
    elif choice == 25:
      testArange(*get_sizes(mode, choice))
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

  np.save("%s/%s/nodes%s.npy"%(mode, instance_id, mode), allNodeDetails)
  np.save("%s/%s/edges%s.npy"%(mode, instance_id, mode), allEdgeDetails)
  np.save("%s/%s/index%s.npy"%(mode, instance_id, mode), nodeEdgeCounts)
  # np.save("/usr/local/lib/python3.9/site-packages/jraph/nodes%s.npy"%mode, allNodeDetails)
  # np.save("/usr/local/lib/python3.9/site-packages/jraph/edges%s.npy"%mode, allEdgeDetails)
  # np.save("/usr/local/lib/python3.9/site-packages/jraph/index%s.npy"%mode, nodeEdgeCounts)
  receiver.clear_cumulative_data()

_, instance_id, num_graphs, mode = sys.argv
instance_id = int(instance_id)
num_graphs = int(num_graphs)

print(instance_id, mode.__hash__())
random.seed(instance_id + mode.__hash__())

if not os.path.exists("%s/%s"%(mode, instance_id)):
    os.makedirs("%s/%s"%(mode, instance_id))

# generateDataset(mode, num_graphs, instance_id)

def predict():
  global receiver
  import numpy as np
  (allNodeDetails, allEdgeDetails, nodeEdgeCounts), times = receiver.receiverData
  def flatten(lol):
    return [i for l in lol for i in l]
  allNodeDetails = np.asarray(flatten(allNodeDetails))
  allEdgeDetails = np.reshape(np.asarray(flatten(allEdgeDetails)), (-1, 4))
  labels = [-1, -1]
  nodeEdgeCounts = np.concatenate([np.asarray(nodeEdgeCounts), np.expand_dims(np.asarray(labels), axis=1)], axis=1)
  patcher.uninstall()
  print("GNN Predicts this as: ", IntToClassMapping[evaluate(allNodeDetails, allEdgeDetails, nodeEdgeCounts)])
  patcher.install()


def testWildImpl():
  import Datasets.Wild.transpose as totest
  a = [[3,4,-2,-5,3], [4,5,6,6,7]]
  # b = 
  # a = 1
  # b = 20
  # c = 5
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)
  


# random.seed(92)
import time
st = time.time()
for i in range(1):
  testWildImpl()
  predict()
en = time.time()
print(en - st)
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
