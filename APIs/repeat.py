import shape, ravel, zeros
import itertools

def repeat_1(a, repeats, axis=None):
    if axis is None:
        a = ravel.ravel_1(a)
        axis = 0
    
    shape_inp = shape.shape_1(a)
    if axis < 0:
        axis += len(shape_inp)
    if shape_inp == ():
        shape_inp = (1,)
        a = [a]

    shape_out = list(shape_inp)
    shape_out[axis] *= repeats
    out_array = zeros.zeros_1(shape_out)
    for indices in itertools.product(*[list(range(j)) for j in shape_out]):
        x = a
        for i, index in enumerate(indices):
            fact = repeats if i == axis else 1
            x = x[index // fact]

        out = out_array
        for i, index in enumerate(indices):
            if i + 1 == len(indices):
                out[index] = x
            else:
                out = out[index]
    
    return out_array

def test_repeat():
    import numpy as np

    assert(np.repeat([3, 5], 4).tolist() == repeat_1([3, 5], 4))
    assert(np.repeat(3, 4).tolist() == repeat_1(3, 4))
    x = np.array([[1,2],[3,4]])
    assert(np.repeat(x, 2).tolist() == repeat_1(x.tolist(), 2))
    assert(np.repeat(x, 3, axis=1).tolist() == repeat_1(x.tolist(), 3, axis=1))

    x = np.array([[1,2, 4, 5],[3,4, 7, 8]])
    assert(np.repeat(x, 5).tolist() == repeat_1(x.tolist(), 5))
    assert(np.repeat(x, 3, axis=-2).tolist() == repeat_1(x.tolist(), 3, axis=-2))