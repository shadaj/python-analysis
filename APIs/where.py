import shape, util
import itertools

def where_1(condition, X, Y):
    c_shape = shape.shape_1(condition)
    X_shape = shape.shape_1(X)
    Y_shape = shape.shape_1(Y)

    c_dim = len(c_shape)
    X_dim = len(X_shape)
    Y_dim = len(Y_shape)

    out_shape = util.broadcast_shape(util.broadcast_shape(X_shape, Y_shape), c_shape)
    out_array = util.create_array(out_shape)
    out_dim = len(out_shape)

    for indices in itertools.product(*[list(range(j)) for j in out_shape]):
        x = X
        for i, index in enumerate(indices[out_dim-X_dim:]):
            x = x[index % X_shape[i]]
        y = Y
        for i, index in enumerate(indices[out_dim-Y_dim:]):
            y = y[index % Y_shape[i]]
        c = condition
        for i, index in enumerate(indices[out_dim-c_dim:]):
            c = c[index % c_shape[i]]

        out = out_array
        for i, index in enumerate(indices):
            if i + 1 == len(indices):
                if c:
                    out[index] = x
                else:
                    out[index] = y
            else:
                out = out[index]

    if len(out_shape) == 0: 	# Not an array
        if condition:
            return X
        else:
            return Y
    else:
        return out_array

def test_where():
    import jax as jax
    import jax.numpy as np
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.where

    A = jrr(key, (2, 2), 0, 5)
    B = jrr(key, (2, 2), 5, 10)
    C = jrr(key, (2, 2), 0, 2)
    assert(op(C, A, B).tolist() == where_1(C.tolist(), A.tolist(), B.tolist()))

    A = jrr(key, (3, 2, 2), 0, 5)
    B = jrr(key, (2, 2), 5, 10)
    C = jrr(key, (2, 2), 0, 2)
    assert(op(C, A, B).tolist() == where_1(C.tolist(), A.tolist(), B.tolist()))

    A = jrr(key, (2, 2), 0, 5)
    B = jrr(key, (3, 2, 2), 5, 10)
    C = jrr(key, (2, 2), 0, 2)
    assert(op(C, A, B).tolist() == where_1(C.tolist(), A.tolist(), B.tolist()))

    A = jrr(key, (2, 2), 0, 5)
    B = jrr(key, (2, 2), 5, 10)
    C = jrr(key, (3, 2, 2), 0, 2)
    assert(op(C, A, B).tolist() == where_1(C.tolist(), A.tolist(), B.tolist()))

    A = jrr(key, (1, 3, 1), 0, 5)
    B = jrr(key, (2, 1, 4), 5, 10)
    C = jrr(key, (1, 3, 4), 0, 2)
    assert(op(C, A, B).tolist() == where_1(C.tolist(), A.tolist(), B.tolist()))

    A = jrr(key, (), 0, 5)
    B = jrr(key, (2, 1, 4), 5, 10)
    C = jrr(key, (1, 3, 4), 0, 2)
    assert(op(C, A, B).tolist() == where_1(C.tolist(), A.tolist(), B.tolist()))

    A = jrr(key, (3, 1), 0, 5)
    B = jrr(key, (2, 1, 4), 5, 10)
    C = jrr(key, (), 0, 2)
    assert(op(C, A, B).tolist() == where_1(C.tolist(), A.tolist(), B.tolist()))

    A = jrr(key, (), 0, 5)
    B = jrr(key, (), 5, 10)
    C = jrr(key, (), 0, 2)
    assert(op(C, A, B).tolist() == where_1(C.tolist(), A.tolist(), B.tolist()))