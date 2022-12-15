import ravel, shape, transpose, zeros_like
import itertools

def argmerge(a):
    a_index = [(a[i], i) for i in range(len(a))]
    a_index = merge2_tuples(a_index)
    ret = [i[1] for i in a_index]
    return ret

def merge2_tuples(a):
    length = len(a)
    if length <= 1:
        return a
    halfway = length // 2
    aLeft = merge2_tuples(a[:halfway])
    aRight = merge2_tuples(a[halfway:])
    i1 = 0
    i2 = 0
    # i1, i2 = 0, 0 #This changes the graph
    t = []
    while i1 != halfway or i2 != length - halfway:
        if i1 == halfway:
            t.append(aRight[i2])
            i2 += 1
        elif i2 == length - halfway:
            t.append(aLeft[i1])
            i1 += 1
        else:
            if aLeft[i1][0] <= aRight[i2][0]:
                t.append(aLeft[i1])
                i1 += 1
            else:
                t.append(aRight[i2])
                i2 += 1
    return t

def argsort_1(a, axis=-1):
    if axis is None:
        a = ravel.ravel_1(a)
        axis = 0

    shape_inp = shape.shape_1(a)
    if axis < 0:
        axis += len(shape_inp)

    transpose_axes = [i for i in range(len(shape_inp))]
    transpose_axes[axis], transpose_axes[-1] = transpose_axes[-1], transpose_axes[axis]

    new_a = transpose.transpose_1(a, transpose_axes)
    new_arg = zeros_like.zeros_like_1(new_a)
    shape_iter = shape.shape_1(new_a)

    for indices in itertools.product(*[list(range(j)) for j in shape_iter[:-1]]):
        a = new_a
        for index in indices:
            a = a[index]
        arg = new_arg
        args_sorted = argmerge(a)
        for index in indices:
            arg = arg[index]
        for i in range(shape_iter[-1]):
            arg[i] = args_sorted[i]

    ret_a = transpose.transpose_1(new_arg, transpose_axes)
    return ret_a

def test_argsort():
    import numpy as np
    op = np.argsort
    myop = argsort_1
    A = np.random.randint(0, 10, size=(1,))
    assert(op(A, None, kind="stable").tolist() == myop(A.tolist(), None))

    A = np.random.randint(0, 10, size=(1,))
    assert(op(A, 0, kind="stable").tolist() == myop(A.tolist(), 0))

    A = np.random.randint(0, 10, size=(1,1))
    assert(op(A, -1, kind="stable").tolist() == myop(A.tolist(), -1))

    A = np.random.randint(0, 10, size=(5,))
    assert(op(A, 0, kind="stable").tolist() == myop(A.tolist(), 0))

    A = np.random.randint(0, 10, size=(4, 5))
    assert(op(A, None, kind="stable").tolist() == myop(A.tolist(), None))

    A = np.random.randint(0, 10, size=(4, 5))
    assert(op(A, 0, kind="stable").tolist() == myop(A.tolist(), 0))

    A = np.random.randint(0, 10, size=(4, 5))
    assert(op(A, 1, kind="stable").tolist() == myop(A.tolist(), 1))

    A = np.random.randint(0, 10, size=(4, 5, 6, 7))
    assert(op(A, 2, kind="stable").tolist() == myop(A.tolist(), 2))

    A = np.random.randint(0, 10, size=(4, 5, 6, 7))
    assert(op(A, None, kind="stable").tolist() == myop(A.tolist(), None))
