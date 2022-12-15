import shape, prod, util
import itertools

def reshape_1(array, newshape):
    or_shape = shape.shape_1(array)

    if isinstance(newshape, int):
        newshape = [newshape]

    cumprod = 1
    index_1 = None
    for i, sh in enumerate(newshape):
        if sh != -1:
            cumprod *= sh
        else:
            index_1 = i
    
    newshape = list(newshape)
    if index_1 is not None:
        missing_index = prod.prod_1(or_shape) // cumprod
        newshape[index_1] = missing_index

    output =  util.create_array(newshape)
    
    for indices_or, indices_new in zip(itertools.product(*[list(range(j)) for j in or_shape]), itertools.product(*[list(range(k)) for k in newshape])):
        a = array
        for index in indices_or:
            a = a[index]
        
        out = output
        for i, index in enumerate(indices_new):
            if i + 1 == len(indices_new):
                out[index] = a
            else:
                out = out[index]

    if len(newshape) == 0: 	# Not an array
        a = array
        for i in or_shape:
            a = a[0]
        return a
    else:
        return output

def test_reshape():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (2, 5, 3, 7), 0, 10)
    assert(np.array_equal(np.reshape(A, -1), np.asarray(reshape_1(A.tolist(), -1))))

    A = jrr(key, (2, 5, 3, 7), 0, 10)
    assert(np.array_equal(np.reshape(A, (7,5,3,2)), np.asarray(reshape_1(A.tolist(), (7,5,3,2)))))

    A = jrr(key, (16,), 0, 10)
    assert(np.array_equal(np.reshape(A, (2,-1,2)), np.asarray(reshape_1(A.tolist(), (2,-1,2)))))

    A = jrr(key, (16,), 0, 10)
    assert(np.array_equal(np.reshape(A, (2,-1,2)), np.asarray(reshape_1(A.tolist(), (2,-1,2)))))

    A = jrr(key, (1,), 0, 10)
    assert(np.array_equal(np.reshape(A, ()), np.asarray(reshape_1(A.tolist(), ()))))

    A = jrr(key, (), 0, 10)
    assert(np.array_equal(np.reshape(A, (1,)), np.asarray(reshape_1(A.tolist(), (1,)))))