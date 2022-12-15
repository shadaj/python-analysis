import ravel, shape, util
import itertools

def take_1(a, indexes, axis=None):
    if axis is None:
        a = ravel.ravel_1(a)
        axis = 0

    shape_inp = shape.shape_1(a)
    dim_inp = len(shape_inp)

    if axis < 0:
        axis += dim_inp

    out_shape = shape_inp[:axis] + shape.shape_1(indexes) + shape_inp[axis+1:]
    last_to_take = len(shape_inp[axis+1:])
    out_array = util.create_array(out_shape)
    out_dim = len(out_shape)
    for indices in itertools.product(*[list(range(j)) for j in out_shape]):
        ind = indexes
        for index in indices[axis:out_dim-last_to_take]:
            ind = ind[index]
        
        x = a
        for index in indices[:axis]:
            x = x[index]
        x = x[ind]
        for index in indices[out_dim-last_to_take:]:
            x = x[index]


        out = out_array
        for i, index in enumerate(indices):
            if i + 1 == len(indices):
                out[index] = x
            else:
                out = out[index]

    if len(out_shape) == 0:
        return a[indexes]
    else:
        return out_array

def test_take():
    import numpy as np

    A = np.random.randint(0, 10, size=(1,))
    ind = 0
    axis = 0
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))

    A = np.random.randint(0, 10, size=(1,))
    ind = 0
    axis = -1
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))

    A = np.random.randint(0, 10, size=(1,))
    ind = [[0, 0], [0, 0]]
    axis = -1
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))

    A = np.random.randint(0, 10, size=(1,1))
    ind = [[0, 0], [0, 0]]
    axis = -1
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))

    A = np.random.randint(0, 10, size=(4, 5, 7))
    ind = 2
    axis = -1
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))

    A = np.random.randint(0, 10, size=(4, 5, 7))
    ind = -1
    axis = 1
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))

    A = np.random.randint(0, 10, size=(4, 5, 7))
    ind = [[0,1],[2,3],[4,-1]]
    axis = 1
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))

    A = np.random.randint(0, 10, size=(4, 5, 7))
    ind = [[0,1],[2,3],[4,-1]]
    axis = None
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))

    A = np.random.randint(0, 10, size=(4, 5, 7))
    ind = 100
    axis = None
    assert(np.take(A, ind, axis).tolist() == take_1(A.tolist(), ind, axis))