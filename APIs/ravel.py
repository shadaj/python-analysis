import reshape

def ravel_1(array):
    return reshape.reshape_1(array, -1)

def test_ravel():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.ravel

    A = jrr(key, (5, 3, 7), 0, 10)
    assert(np.array_equal(op((A)), np.asarray(ravel_1(A.tolist()))))

    A = jrr(key, (), 0, 10)
    assert(np.array_equal(op((A)), np.asarray(ravel_1(A.tolist()))))