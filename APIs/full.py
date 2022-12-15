def full_1(shape, val):
    if isinstance(shape, int):
        return [val] * shape
    elif len(shape) == 0:
        return val
    else:
        return [full_1(shape[1:], val) for i in range(shape[0])]

def test_zeros():
    import jax.numpy as np
    
    A = np.full((1,), 6)
    assert(np.array_equal(A, np.asarray(full_1((1,), 6))))

    A = np.full((2, 3, 5), 7)
    assert(np.array_equal(A, np.asarray(full_1((2, 3, 5), 7))))

    A = np.full((), 9)
    assert(np.array_equal(A, np.asarray(full_1((), 9))))