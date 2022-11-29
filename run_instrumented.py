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

def get_broadcast_compatible_shape(original1, original2, max_dim):
  import numpy as np
  or1 = list(original1)
  or2 = list(original2)
  original = []
  while len(or1) > 0 or len(or2) > 0:
    if len(or1) > 0 and len(or2) > 0:
      el = min(or1.pop(), or2.pop())
    elif len(or1) > 0:
      el = or1.pop()
    else:
      el = or2.pop()
    original.append(el)
  original = original[::-1]
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

def get_random_init(dims, dim_size_max):
  import numpy as np
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  return size_a, size_b, a, b

def get_random_init_element_wise(dims, dim_size_max):
  import numpy as np
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = get_broadcast_compatible_shape(size_a, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  return size_a, size_b, a, b

def get_random_init_element_wise_3(dims, dim_size_max):
  import numpy as np
  size_a = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = get_broadcast_compatible_shape(size_a, dim_size_max)
  size_c = get_broadcast_compatible_shape(size_a, size_b, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  c = np.random.uniform(low=-10., high=10., size=size_c).tolist()
  return size_a, size_b, size_c, a, b, c

def get_random_init_reduction(dims, dim_size_max):
  import numpy as np
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_where = get_broadcast_compatible_shape(size, dim_size_max)
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size), size=np.random.choice(len(size)), replace=False).tolist()]) 
  keepdims = np.random.choice([None, True])
  initial = np.random.choice([None, 1])
  where = np.random.choice([None, np.random.choice([True, False], size=size_where).tolist()])
  return size, size_where, a, axis, keepdims, initial, where

def get_random_init_complex_reduction(dims, dim_size_max):
  import numpy as np
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  axis = np.random.choice([None, np.random.choice(len(size)).tolist()]) 
  keepdims = np.random.choice([None, True])
  return size, a, axis, keepdims

###### DATASET GENERATORS

### REDUCTION

def testReductionSum(dims, dim_size_max):
  import numpy as np
  import APIs.sum as sum
  size, size_where, a, axis, keepdims, initial, where = get_random_init_reduction(dims, dim_size_max)
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
  size, size_where, a, axis, keepdims, initial, where = get_random_init_reduction(dims, dim_size_max)
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
  size, size_where, a, axis, keepdims, initial, where = get_random_init_reduction(dims, dim_size_max)
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
  size, size_where, a, axis, keepdims, initial, where = get_random_init_reduction(dims, dim_size_max)
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
  size, size_where, a, axis, keepdims, _, where = get_random_init_reduction(dims, dim_size_max)
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
  size, size_where, a, axis, keepdims, _, where = get_random_init_reduction(dims, dim_size_max)
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
  size, size_where, a, axis, keepdims, _, where = get_random_init_reduction(dims, dim_size_max)
  print(a, size)
  print(axis)
  print(keepdims)
  print(where, size_where)
  with receiver:
    ans = any.any_1(a, axis=axis, keepdims=keepdims, where=where)
  print("reduction any: ", ans)

def testReductionCountNonzero(dims, dim_size_max):
  import numpy as np
  import APIs.count_nonzero as count_nonzero
  size, _, a, axis, keepdims, _, _ = get_random_init_reduction(dims, dim_size_max)
  print(a, size)
  print(axis)
  print(keepdims)
  with receiver:
    ans = count_nonzero.count_nonzero_1(a, axis=axis, keepdims=keepdims)
  print("reduction count_nonzero: ", ans)

def testReductionStd(dims, dim_size_max):
  import numpy as np
  import APIs.std as std
  size, size_where, a, axis, keepdims, _, where = get_random_init_reduction(dims, dim_size_max)
  print(a, size)
  print(axis)
  print(keepdims)
  print(where, size_where)
  with receiver:
    ans = std.std_1(a, axis=axis, keepdims=keepdims, where=where)
  print("reduction std: ", ans)

### ELEMENT-WISE

def testAdd(dims, dim_size_max):
  import numpy as np
  import APIs.add as add
  size_a, size_b, a, b = get_random_init_element_wise(dims, dim_size_max)
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = add.add_1(a, b)
  print("add: ", ans)

def testWhere(dims, dim_size_max):
  import numpy as np
  import APIs.where as where
  size_a, size_b, size_c, a, b, c = get_random_init_element_wise_3(dims, dim_size_max)
  print(a, size_a)
  print(b, size_b)
  print(c, size_c)
  with receiver:
    ans = where.where_1(a, b, c)
  print("where: ", ans)

### COMPLEX REDUCTION

def testReductionCumsum(dims, dim_size_max):
  import numpy as np
  import APIs.cumsum as cumsum
  size, a, axis, _ = get_random_init_complex_reduction(dims, dim_size_max)
  print(a, size)
  print(axis)
  with receiver:
    ans = cumsum.cumsum_1(a, axis=axis)
  print("reduction cumsum: ", ans)

def testReductionArgmax(dims, dim_size_max):
  import numpy as np
  import APIs.argmax as argmax
  size, a, axis, keepdims = get_random_init_complex_reduction(dims, dim_size_max)
  print(a, size)
  print(axis)
  print(keepdims)
  with receiver:
    ans = argmax.argmax_1(a, axis=axis, keepdims=keepdims)
  print("reduction argmax: ", ans)

def testReductionArgmin(dims, dim_size_max):
  import numpy as np
  import APIs.argmin as argmin
  size, a, axis, keepdims = get_random_init_complex_reduction(dims, dim_size_max)
  print(a, size)
  print(axis)
  print(keepdims)
  with receiver:
    ans = argmin.argmin_1(a, axis=axis, keepdims=keepdims)
  print("reduction argmin: ", ans)

### MATH OPERATIONS

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

def testMatmul(dims, dim_size_max):
  import numpy as np
  import APIs.matmul as matmul
  size_a = ([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  size_b = ([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  if len(size_b) == 1:
    size_b[-1] = size_a[-1]
  elif len(size_b) >= 2:
    size_b[-2] = size_a[-1]
    size_b[:-2] = get_broadcast_compatible_shape(size_a[:-2], dim_size_max)
  size_a = tuple(size_a)
  size_b = tuple(size_b)
  a = np.random.uniform(low=-10., high=10., size=size_a).tolist()
  b = np.random.uniform(low=-10., high=10., size=size_b).tolist()
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = matmul.matmul_1(a, b)
  print("matmul: ", ans)

def testOuter(dims, dim_size_max):
  import numpy as np
  import APIs.outer as outer
  size_a, size_b, a, b = get_random_init(dims, dim_size_max)
  print(a, size_a)
  print(b, size_b)
  with receiver:
    ans = outer.outer_1(a, b)
  print("outer: ", ans)

def testClip(dims, dim_size_max):
  import numpy as np
  import APIs.clip as clip
  size_a, _, a, _ = get_random_init(dims, dim_size_max)
  lim1 = np.random.choice([-5, -15])
  lim2 = np.random.choice([5, 15])
  print(a, size_a)
  with receiver:
    ans = clip.clip_1(a, lim1, lim2)
  print("clip: ", ans)

def testDiff(dims, dim_size_max):
  import numpy as np
  import APIs.diff as diff
  size, a, axis, _ = get_random_init_complex_reduction(dims, dim_size_max)
  n = np.random.choice([1,2])
  print(a, size)
  with receiver:
    ans = diff.diff_1(a, n, axis)
  print("diff: ", ans)

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

def testAllclose(dims, dim_size_max):
  import numpy as np
  import APIs.allclose as allclose
  size_a, size_b, a, b = get_random_init_element_wise(dims, dim_size_max)
  rtol = np.random.choice([1e-5, 1e-4])
  atol = np.random.choice([1e-8, 1e-7])
  if np.random.choice(0, 2):
    b = a
    size_b = size_a
  equal_nan = np.random.choice([True, False])
  print(size_a, a)
  print(size_b, b)
  print(rtol, atol, equal_nan) 
  with receiver:
    ans = allclose.allclose_1(a, b, rtol, atol, equal_nan)
  print("allclose: ", ans)

### SHAPE MANIPULATION

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

def testRavel(dims, dim_size_max):
  import numpy as np
  import APIs.ravel as ravel

  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  print(a, size)
  with receiver:
    ans = ravel.ravel_1(a)
  print("ravel: ", ans)

def testMoveaxis(dims, dim_size_max):
  import numpy as np
  import APIs.moveaxis as moveaxis
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  source = np.random.choice(len(size))
  destination = np.random.choice(len(size))
  with receiver:
    ans = moveaxis.moveaxis_1(a, source, destination)
  print("moveaxis: ", ans)

def testSqueeze(dims, dim_size_max):
  import numpy as np
  import APIs.squeeze as squeeze
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  with receiver:
    ans = squeeze.squeeze_1(a)
  print("squeeze: ", ans)

def testReshape(dims, dim_size_max):
  import numpy as np
  import APIs.reshape as reshape
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  newshape = np.random.permutation(size)
  with receiver:
    ans = reshape.reshape_1(a, newshape)
  print("reshape: ", ans)

def testAtleast1D(dims, dim_size_max):
  import numpy as np
  import APIs.atleast_1d as atleast_1d
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  with receiver:
    ans = atleast_1d.atleast_1d_1(a)
  print("atleast 1d: ", ans)

### LINEAR OPERATIONS: MULTIPLE ARGUMENTS

def testConcatenate(dims, dim_size_max):
  import numpy as np
  import APIs.concatenate as concatenate
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  axis = np.random.choice([None, np.random.randint(2, len(size))])
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

def testVstack(dims, dim_size_max):
  import numpy as np
  import APIs.vstack as vstack
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  N = np.random.randint(1, dims+1) # Number of arrays to concatenate, using dims variable
  arrays = []
  for i in range(N):
    if len(size) != 1:
      size_ = list(size)
      size_[0] = np.random.randint(1, dim_size_max+1) # Concatenated axis may be different in all operands
    else:
      size_ = list(size)
    a = np.random.uniform(low=-10., high=10., size=size_).tolist()
    print(a, size_)
    arrays.append(a)
  with receiver:
    ans = vstack.vstack_1(arrays)
  print("vstack: ", ans)

def testHstack(dims, dim_size_max):
  import numpy as np
  import APIs.hstack as hstack
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  N = np.random.randint(1, dims+1) # Number of arrays to concatenate, using dims variable
  arrays = []
  for i in range(N):
    if len(size) != 1:
      size_ = list(size)
      size_[1] = np.random.randint(1, dim_size_max+1) # Concatenated axis may be different in all operands
    else:
      size_ = tuple([np.random.randint(1,dim_size_max+1)])
    a = np.random.uniform(low=-10., high=10., size=size_).tolist()
    print(a, size_)
    arrays.append(a)
  with receiver:
    ans = hstack.hstack_1(arrays)
  print("vstack: ", ans)

def testStack(dims, dim_size_max):
  import numpy as np
  import APIs.stack as stack
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  axis = np.random.choice([np.random.randint(0, 1+len(size))])
  N = np.random.randint(1, dims+1) # Number of arrays to concatenate, using dims variable
  arrays = []
  print(axis)
  for i in range(N):
    a = np.random.uniform(low=-10., high=10., size=size).tolist()
    print(a, size)
    arrays.append(a)
  with receiver:
    ans = stack.stack_1(axis, arrays)
  print("stack: ", ans)

def testTile(dims, dim_size_max):
  import numpy as np
  import APIs.tile as tile
  size = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  a = np.random.uniform(low=-10., high=10., size=size).tolist()
  reps = np.random.choice(np.arange(1,dim_size_max+1), size=np.random.choice(dims)).tolist()
  print(a, size)
  print(reps)
  with receiver:
    ans = tile.tile_1(a, reps)
  print("tile: ", ans)

def testAppend(dims, dim_size_max):
  import numpy as np
  import APIs.append as append
  size, arr, axis, _ = get_random_init_complex_reduction(dims, dim_size_max)
  size_values = list(size)
  if axis is not None:
    size_values[axis] = np.random.randint(1, dim_size_max+1) # Concatenated axis may be different in all operands
  else:
    size_values = tuple([np.random.randint(1,dim_size_max+1) for i in range(np.random.randint(1, dims+1))])
  values = np.random.uniform(low=-10., high=10., size=size_values).tolist()
  print(arr, size)
  print(values, size_values)
  print(axis)
  with receiver:
    ans = append.append_1(arr, values, axis)
  print("append: ", ans)

def testInsert(dims, dim_size_max):
  import numpy as np
  import APIs.insert as insert
  size, arr, axis, _ = get_random_init_complex_reduction(dims, dim_size_max)
  index = np.random.choice(size[axis])
  value = np.random.randint(-10, 10)
  print(arr, size)
  with receiver:
    ans = insert.insert_1(arr, index, value, axis)
  print("insert: ", ans)

def testRepeat(dims, dim_size_max):
  import numpy as np
  import APIs.repeat as repeat
  size, a, axis, _ = get_random_init_complex_reduction(dims, dim_size_max)
  repeats = np.random.choice(dim_size_max)
  print(a, size)
  with receiver:
    ans = repeat.repeat_1(a, repeats, axis)
  print("repeats: ", ans)

### INITIALIZERS

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
  import Datasets.Wild.max as totest
  import numpy as np
  length = 3
  a = np.random.randint(-10, 10, length).tolist()
  # b = 
  # a = 1
  # b = 20
  # c = 5
  print("inp: ", a)
  with receiver:
    ans = totest.func1(a)
  print("ans: ", ans)
  

# for i in range(1000):
#   testReductionMax(2, 6)
# import matplotlib.pyplot as plt
# print("NJDKASBNIJ")
# plt.hist([i[0] for i in shapes1 if len(i) == 1])
# plt.show()
# random.seed(92)
import time
st = time.time()
for i in range(1):
  # testWildImpl()
  # testMergeSort()
  testReductionMean(1, 6)
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
