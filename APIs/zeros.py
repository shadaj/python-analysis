def zeros_1(shape):
    if isinstance(shape, int):
        return [0] * shape
    elif len(shape) == 0:
        return 0
    else:
        return [zeros_1(shape[1:]) for i in range(shape[0])]

def test_zeros():
    import jax.numpy as np
    
    A = np.zeros((3,5))
    assert(np.array_equal(A, np.asarray(zeros_1((3,5)))))

    A = np.zeros(())
    assert(np.array_equal(A, np.asarray(zeros_1(()))))