import shape, reshape, util
import itertools

def tile_1(A, reps):
    if isinstance(reps, int):
        reps = (reps,)
    if not isinstance(A, list):
        A = [A]
    shape_a = shape.shape_1(A)
    if len(shape_a) < len(reps):
        newshape = (1,) * (len(reps) - len(shape_a)) + shape_a
        A = reshape.reshape_1(A, newshape)
        shape_a = shape.shape_1(A)
    else:
        reps = ((1,) * (len(shape_a) - len(reps))) + reps

    output_shape = []
    for i in range(len(reps)):
        output_shape.append(shape_a[i] * reps[i])
    out_array = util.create_array(output_shape)


    for indices in itertools.product(*[list(range(j)) for j in output_shape]):
        out = out_array
        a = A
        for i, index in enumerate(indices):
            a = a[index % shape_a[i]]
        for i, index in enumerate(indices):
            if i + 1 == len(indices):
                out[index] = a
            else:
                out = out[index]
        
    return out_array

def test_tile():
    import numpy as np
    a = np.array([0, 1, 2])
    assert(np.tile(a, 2).tolist() == tile_1(a.tolist(), 2))
    assert(np.tile(a, (2, 3)).tolist() == tile_1(a.tolist(), (2, 3)))
    assert(np.tile(a, (2, 1, 2)).tolist() == tile_1(a.tolist(), (2, 1, 2)))
    a = np.array([[1, 2], [3, 4]])
    assert(np.tile(a, 2).tolist() == tile_1(a.tolist(), 2))
    assert(np.tile(a, (2, 1)).tolist() == tile_1(a.tolist(), (2, 1)))
    a = np.array([1,2,3,4])
    assert(np.tile(a, (4, 1)).tolist() == tile_1(a.tolist(), (4, 1)))
    a = 2
    assert(np.tile(a, (4, 2)).tolist() == tile_1(a, (4, 2)))


