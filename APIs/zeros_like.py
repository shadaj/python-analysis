import shape as sh
import zeros

def zeros_like_1(a):
    shape = sh.shape_1(a)
    if isinstance(shape, int):
        return [0] * shape
    elif len(shape) == 0:
        return 0
    else:
        return [zeros.zeros_1(shape[1:]) for i in range(shape[0])]

def test_zeros_like():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (8, 1, 2, 1, 3, 1), 0, 10)
    assert(np.array_equal(np.zeros_like(A), np.asarray(zeros_like_1(A.tolist()))))

    A = jrr(key, (), 0, 10)
    assert(np.array_equal(np.zeros_like(A), np.asarray(zeros_like_1(A.tolist()))))