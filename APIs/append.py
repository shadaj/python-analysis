import ravel, concatenate
import itertools

def append_1(arr, values, axis=None):
    if axis is None:
        return ravel.ravel_1(arr) + ravel.ravel_1(values)
    else:
        return concatenate.concatenate_1(axis, arr, values)

def test_append():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.append

    A = jrr(key, (2, 4, 7), 0, 10)
    B = jrr(key, (2, 3, 7), 0, 10)
    assert(np.array_equal(op(A, B, 1),np.asarray(append_1(A.tolist(), B.tolist(), 1))))

    A = jrr(key, (7, 5), 0, 10)
    B = jrr(key, (7, 2), 0, 10)
    assert(np.array_equal(op(A, B, -1),np.asarray(append_1(A.tolist(), B.tolist(), -1))))

    A = jrr(key, (), 0, 10)
    B = jrr(key, (), 0, 10)
    assert(np.array_equal(op(A, B),np.asarray(append_1(A.tolist(), B.tolist()))))

    A = jrr(key, (5,), 0, 10)
    B = jrr(key, (9,), 0, 10)
    assert(np.array_equal(op(A, B),np.asarray(append_1(A.tolist(), B.tolist()))))