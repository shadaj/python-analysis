import ravel, shape, transpose, zeros, add, concatenate

def insert_1(arr, indices, values, axis=None):
    if axis is None:
        arr = ravel.ravel_1(arr)
        axis = 0
    
    shape_inp = shape.shape_1(arr)
    dim_inp = len(shape_inp)

    if axis < 0:
        axis += dim_inp

    if isinstance(indices, int):
        indices = [indices]

    transpose_axis = [i for i in range(dim_inp)]
    transpose_axis[0], transpose_axis[axis] = transpose_axis[axis], transpose_axis[0]

    a_t = transpose.transpose_1(arr, transpose_axis)

    a_t_split = []
    indices.append(None)
    indices = [0] + indices
    for i in range(1, len(indices)):
        a_t_split.append(a_t[indices[i-1]:indices[i]])
    
    shape_toadd = list(shape_inp)
    shape_toadd[0], shape_toadd[axis] = shape_toadd[axis], shape_toadd[0]
    shape_toadd[0] = 1

    to_add = zeros.zeros_1(shape_toadd)
    to_add = add.add_1(to_add, values)

    res = None
    for i, el in enumerate(a_t_split):
        if res is None:
            res = concatenate.concatenate_1(0, el, to_add)
        elif i + 1 == len(a_t_split):
            res = concatenate.concatenate_1(0, res, el)
        else:
            res = concatenate.concatenate_1(0, res, el, to_add)
        
    return transpose.transpose_1(res, transpose_axis)

def test_insert():
    import numpy as np

    A = np.random.randint(0, 10, size=(1,))
    for axis in [0,-1,None]:
        assert(np.insert(A, 0, 11, axis).tolist() == insert_1(A.tolist(), 0, 11, axis))
        assert(np.insert(A, -1, 11, axis).tolist() == insert_1(A.tolist(), -1, 11, axis))

    A = np.random.randint(0, 10, size=(2, 2))
    for axis in [0,1,-1,None]:
        assert(np.insert(A, 1, 11, axis).tolist() == insert_1(A.tolist(), 1, 11, axis))
        assert(np.insert(A, 0, 11, axis).tolist() == insert_1(A.tolist(), 0, 11, axis))
        assert(np.insert(A, -1, 11, axis).tolist() == insert_1(A.tolist(), -1, 11, axis))

    A = np.random.randint(0, 10, size=(3, 4, 5))
    for axis in [0,1,-1,None]:
        assert(np.insert(A, 1, 11, axis).tolist() == insert_1(A.tolist(), 1, 11, axis))
        assert(np.insert(A, 0, 11, axis).tolist() == insert_1(A.tolist(), 0, 11, axis))
        assert(np.insert(A, -1, 11, axis).tolist() == insert_1(A.tolist(), -1, 11, axis))

    A = np.random.randint(0, 10, size=(3, 4, 5, 7))
    for axis in [0,1,-1,None]:
        assert(np.insert(A, 1, 11, axis).tolist() == insert_1(A.tolist(), 1, 11, axis))
        assert(np.insert(A, 0, 11, axis).tolist() == insert_1(A.tolist(), 0, 11, axis))
        assert(np.insert(A, -1, 11, axis).tolist() == insert_1(A.tolist(), -1, 11, axis))