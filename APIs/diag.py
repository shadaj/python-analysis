import shape, zeros

def diag_1(v, k = 0):
    shp = shape.shape_1(v)
    dim = len(shp)

    if dim == 2:
        output = []
        if k >= 0:
            i1 = 0
            i2 = k
        else:
            i1 = -k
            i2 = 0
        while i1 < shp[0] and i2 < shp[1]:
            output.append(v[i1][i2])
            i1 += 1
            i2 += 1
    elif dim == 1:
        kabs = k if k > 0 else -k
        output = zeros.zeros_1((shp[0] + kabs, shp[0] + kabs))
        if k >= 0:
            i1 = 0
            i2 = k
        else:
            i1 = -k
            i2 = 0
        for i in range(shp[0]):
            output[i+i1][i+i2] = v[i]
    return output

def test_diag():
    import jax as jax
    import jax.numpy as np
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.diag

    
    A = jrr(key, (1,), 0, 5)
    k = 0
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (1,1), 0, 5)
    k = 0
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (1,1), 0, 5)
    k = 1
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (1,1), 0, 5)
    k = -2
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (10,), 0, 5)
    k = -2
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (10,), 0, 5)
    k = 3
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (10,), 0, 5)
    k = 0
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (10,11), 0, 5)
    k = 4
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (10,11), 0, 5)
    k = -5
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))

    A = jrr(key, (10,11), 0, 5)
    k = 0
    assert(op(A, k).tolist() == diag_1(A.tolist(), k))