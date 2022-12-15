import ravel, shape, zeros

def outer_1(X, Y):
    X_ravelled = ravel.ravel_1(X)
    Y_ravelled = ravel.ravel_1(Y)

    x_shape = shape.shape_1(X_ravelled)
    y_shape = shape.shape_1(Y_ravelled)

    M = x_shape[0]
    N = y_shape[0]
    output = zeros.zeros_1((M, N))

    for i in range(M):
        for j in range(N):
            output[i][j] = X_ravelled[i] * Y_ravelled[j]

    return output

def test_outer():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (8, 5), 0, 10)
    B = jrr(key, (2, 7, 1), 0, 10)
    op = np.outer
    assert(op(A, B).tolist() == outer_1(A.tolist(), B.tolist()))

    A = jrr(key, (1,), 0, 10)
    B = jrr(key, (2, 5, 7), 0, 10)
    assert(op(A, B).tolist() == outer_1(A.tolist(), B.tolist()))

    A = jrr(key, (), 0, 10)
    B = jrr(key, (), 0, 10)
    assert(op(A, B).tolist() == outer_1(A.tolist(), B.tolist()))

    A = jrr(key, (1,), 0, 10)
    B = jrr(key, (), 0, 10)
    assert(op(A, B).tolist() == outer_1(A.tolist(), B.tolist()))