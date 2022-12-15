import shape, reshape

def atleast_1d_1(array):
    shape_array = shape.shape_1(array)

    if len(shape_array) < 1:
        shape_array = (1,)
        return reshape.reshape_1(array, shape_array)
    else:
        return array

def test_atleast_1d():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (), 0, 10)
    assert(np.array_equal(np.atleast_1d(A), np.asarray(atleast_1d_1(A.tolist()))))
    A = jrr(key, (1,), 0, 10)
    assert(np.array_equal(np.atleast_1d(A), np.asarray(atleast_1d_1(A.tolist()))))
    A = jrr(key, (2, 3), 0, 10)
    assert(np.array_equal(np.atleast_1d(A), np.asarray(atleast_1d_1(A.tolist()))))