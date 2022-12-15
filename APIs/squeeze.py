import shape, reshape

def squeeze_1(a, axis=None):
    shp = shape.shape_1(a)

    out_shp = []
    if axis is None:
        for s in shp:
            if not s == 1:
                out_shp.append(s)
    else:
        if isinstance(axis, int):
            axis = [axis]
        for i in range(len(axis)):
            if axis[i] < 0:
                axis[i] += len(shp)
        for i, s in enumerate(shp):
            if i in axis:
                if s == 1:
                    continue
            out_shp.append(s)
    
    return reshape.reshape_1(a, out_shp)

def test_squeeze():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.squeeze

    A = jrr(key, (1, 3, 1), 0, 10)
    assert(np.array_equal(op(A, None),np.asarray(squeeze_1(A.tolist(), None))))

    A = jrr(key, (1, 1), 0, 10)
    assert(np.array_equal(op(A, None),np.asarray(squeeze_1(A.tolist(), None))))

    A = jrr(key, (2, 3, 4), 0, 10)
    assert(np.array_equal(op(A, None),np.asarray(squeeze_1(A.tolist(), None))))

    A = jrr(key, (1,), 0, 10)
    assert(np.array_equal(op(A, None),np.asarray(squeeze_1(A.tolist(), None))))

    A = jrr(key, (), 0, 10)
    assert(np.array_equal(op(A, None),np.asarray(squeeze_1(A.tolist(), None))))

    A = jrr(key, (1, 1), 0, 10)
    assert(np.array_equal(op(A, -1),np.asarray(squeeze_1(A.tolist(), -1))))

    A = jrr(key, (1, 3, 1), 0, 10)
    assert(np.array_equal(op(A, 2),np.asarray(squeeze_1(A.tolist(), 2))))

