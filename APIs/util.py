import itertools

import shape as sh

def broadcast_shape(shape_a, shape_b):
    shape_out = []
    length = max(len(shape_a), len(shape_b))
    for i in range(-1, -length - 1, -1):
        a_dim = shape_a[i] if -i <= len(shape_a) else 0
        b_dim = shape_b[i] if -i <= len(shape_b) else 0
        assert (a_dim == b_dim) or a_dim <= 1 or b_dim <= 1, "Unbroadcastable"
        shape_out.append(max(a_dim, b_dim))
    return tuple(shape_out[::-1])

def broadcast_to(arr, shape):
    broadcasted_arr = create_array(shape)
    out_dim = len(shape)
    orig_shape = sh.shape_1(arr)
    arr_dim = len(orig_shape)
    for indices in itertools.product(*[list(range(j)) for j in shape]):
        x = arr
        for i, index in enumerate(indices[out_dim-arr_dim:]):
            x = x[index % orig_shape[i]]
        
        out = broadcasted_arr
        for i, index in enumerate(indices):
            if i + 1 == len(indices):
                out[index] = x
            else:
                out = out[index]
    return broadcasted_arr
        

def create_array(shape):
    if isinstance(shape, int):
        return [0] * shape
    elif len(shape) == 0:
        return 0
    else:
        return [create_array(shape[1:]) for i in range(shape[0])]

def trues(shape):
    if isinstance(shape, int):
        return [True] * shape
    elif len(shape) == 0:
        return True
    else:
        return [trues(shape[1:]) for i in range(shape[0])]

def falses(shape):
    if isinstance(shape, int):
        return [False] * shape
    elif len(shape) == 0:
        return False
    else:
        return [falses(shape[1:]) for i in range(shape[0])]

def nones(shape):
    if isinstance(shape, int):
        return [None] * shape
    elif len(shape) == 0:
        return None
    else:
        return [nones(shape[1:]) for i in range(shape[0])]