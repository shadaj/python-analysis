import ravel, shape, transpose
import itertools

def quick1(a, st=0, en=None):
	if en is None: en=len(a)
	if en-st <= 1:
		return
	pivot = a[st]
	start = st+1
	end = en-1
	while end > start:
		while a[start] <= pivot and start < en-1:
			start += 1
		while pivot <= a[end] and end >= start:
			end -= 1
		if end >= start:
			a[start], a[end] = a[end], a[start]
	if a[end] > pivot:
		a[end-1], a[st] = a[st], a[end-1]
		quick1(a, st, end-1)
		quick1(a, end, en)
	elif a[end] <= pivot:
		a[end], a[st] = a[st], a[end]
		quick1(a, st, end)
		quick1(a, end+1, en)

def sort_1(a, axis=-1):
    if axis is None:
        a = ravel.ravel_1(a)
        axis = 0

    shape_inp = shape.shape_1(a)
    if axis < 0:
        axis += len(shape_inp)

    transpose_axes = [i for i in range(len(shape_inp))]
    transpose_axes[axis], transpose_axes[-1] = transpose_axes[-1], transpose_axes[axis]

    new_a = transpose.transpose_1(a, transpose_axes)
    shape_iter = shape.shape_1(new_a)

    for indices in itertools.product(*[list(range(j)) for j in shape_iter[:-1]]):
        a = new_a
        for index in indices:
            a = a[index]
        quick1(a)

    ret_a = transpose.transpose_1(new_a, transpose_axes)
    return ret_a

def test_sort():
    import numpy as np

    A = np.random.randint(0, 10, size=(1,))
    assert(np.sort(A, None).tolist() == sort_1(A.tolist(), None))

    A = np.random.randint(0, 10, size=(1,))
    assert(np.sort(A, 0).tolist() == sort_1(A.tolist(), 0))

    A = np.random.randint(0, 10, size=(1,1))
    assert(np.sort(A, -1).tolist() == sort_1(A.tolist(), -1))

    A = np.random.randint(0, 10, size=(4, 5))
    assert(np.sort(A, None).tolist() == sort_1(A.tolist(), None))

    A = np.random.randint(0, 10, size=(4, 5))
    assert(np.sort(A, 0).tolist() == sort_1(A.tolist(), 0))

    A = np.random.randint(0, 10, size=(4, 5))
    assert(np.sort(A, 1).tolist() == sort_1(A.tolist(), 1))

    A = np.random.randint(0, 10, size=(4, 5, 6, 7))
    assert(np.sort(A, 2).tolist() == sort_1(A.tolist(), 2))

    A = np.random.randint(0, 10, size=(4, 5, 6, 7))
    assert(np.sort(A, None).tolist() == sort_1(A.tolist(), None))
