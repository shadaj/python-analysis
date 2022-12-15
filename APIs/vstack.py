import shape, reshape, concatenate, itertools

def vstack_1(*arrays):

    input_to_concatenate = [0]
    for array in arrays:
        or_shape = shape.shape_1(array)
        if len(or_shape) == 0:
            new_shape = (1, 1)
            input_to_concatenate.append(reshape.reshape_1(array, new_shape))
        elif len(or_shape) == 1:
            new_shape = (1, ) + or_shape
            input_to_concatenate.append(reshape.reshape_1(array, new_shape))
        else:
            input_to_concatenate.append(array)
    return concatenate.concatenate_1(*input_to_concatenate)

def test_vstack():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.vstack

    A = jrr(key, (5, 3, 7), 0, 10)
    B = jrr(key, (3, 3, 7), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(vstack_1(A.tolist(), B.tolist()))))

    A = jrr(key, (5, 7), 0, 10)
    B = jrr(key, (2, 7), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(vstack_1(A.tolist(), B.tolist()))))

    A = jrr(key, (5, 7), 0, 10)
    B = jrr(key, (7,), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(vstack_1(A.tolist(), B.tolist()))))

    A = jrr(key, (5,), 0, 10)
    B = jrr(key, (5,), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(vstack_1(A.tolist(), B.tolist()))))

    A = jrr(key, (), 0, 10)
    B = jrr(key, (), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(vstack_1(A.tolist(), B.tolist()))))

    A = jrr(key, (1,), 0, 10)
    B = jrr(key, (), 0, 10)
    assert(np.array_equal(op((A, B)),np.asarray(vstack_1(A.tolist(), B.tolist()))))

