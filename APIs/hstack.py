import shape, concatenate

def hstack_1(*arrays):
    or_dims = len(shape.shape_1(arrays[0]))
    if or_dims == 0:
        return arrays
    elif or_dims == 1:
        ls = (0, ) + arrays
        return concatenate.concatenate_1(*ls)
    else:
        ls = (1, ) + arrays
        return concatenate.concatenate_1(*ls)

def test_hstack():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.hstack

    A = jrr(key, (2, 4, 7), 0, 10)
    B = jrr(key, (2, 3, 7), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(hstack_1(A.tolist(), B.tolist()))))

    A = jrr(key, (7, 5), 0, 10)
    B = jrr(key, (7, 2), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(hstack_1(A.tolist(), B.tolist()))))

    A = jrr(key, (), 0, 10)
    B = jrr(key, (), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(hstack_1(A.tolist(), B.tolist()))))

    A = jrr(key, (5,), 0, 10)
    B = jrr(key, (5,), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(hstack_1(A.tolist(), B.tolist()))))