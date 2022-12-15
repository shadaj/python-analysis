import shape, util
import itertools

def abs(m):
    return m if m > 0 else -m

def allclose_1(X, Y, rtol=1e-5, atol=1e-8, equal_nan=False):
    X_shape = shape.shape_1(X)
    Y_shape = shape.shape_1(Y)

    X_dim = len(X_shape)
    Y_dim = len(Y_shape)

    out_shape = util.broadcast_shape(X_shape, Y_shape)
    out_dim = len(out_shape)
    for indices in itertools.product(*[list(range(j)) for j in out_shape]):
        x = X
        for i, index in enumerate(indices[out_dim-X_dim:]):
            x = x[index % X_shape[i]]
        y = Y
        for i, index in enumerate(indices[out_dim-Y_dim:]):
            y = y[index % Y_shape[i]]

        if equal_nan:
            if x!=x and y!=y:
                continue
            elif x!=x or y!=y:
                return False
        else:
            if x!=x or y!=y:
                return False
        if abs(x-y) > atol + rtol * abs(y):
            return False

    if len(out_shape) == 0: 	# Not an array
        if equal_nan:
            if X!=X and Y!=Y:
                return True
            elif X!=X or Y!=Y:
                return False
        else:
            if X!=X or Y!=Y:
                return False
        if abs(X-Y) > atol + rtol * abs(Y):
            return False
        else:
            return True
    else:
        return True


def test_allclose():
    import numpy as np
    op = np.allclose

    A = [1e10,1e-7]
    B = [1.00001e10,1e-8]
    assert(op(np.asarray(A), np.asarray(B)) == allclose_1(A, B))

    A = [1e10,1e-8]
    B = [1.00001e10,1e-9]
    assert(op(np.asarray(A), np.asarray(B)) == allclose_1(A, B))

    A = [1e10,1e-8]
    B = [1.0001e10,1e-9]
    assert(op(np.asarray(A), np.asarray(B)) == allclose_1(A, B))

    A = [1.0, np.nan]
    B = [1.0, np.nan]
    assert(op(np.asarray(A), np.asarray(B)) == allclose_1(A, B))

    A = [1.0, np.nan]
    B = [1.0, np.nan]
    assert(op(np.asarray(A), np.asarray(B), equal_nan=True) == allclose_1(A, B, equal_nan=True))