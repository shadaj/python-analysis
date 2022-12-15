def shape_1(array):
    shape = []
    while type(array) is list or type(array) is tuple:
        shape.append(len(array))
        if len(array) == 0:
            break
        array = array[0]
    return tuple(shape)

def test_shape():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (2, 5, 3, 7), 0, 10)
    assert(np.array_equal(np.shape(A), np.asarray(shape_1(A.tolist()))))

    A = jrr(key, (), 0, 10)
    assert(np.array_equal(np.shape(A), np.asarray(shape_1(A.tolist()))))