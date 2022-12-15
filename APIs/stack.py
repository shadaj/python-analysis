import shape, reshape, concatenate
import itertools

def stack_1(axis = 0, *arrays):
    or_shape = shape.shape_1(arrays[0])
    or_dims = len(or_shape)
    new_shape = []
    if axis < 0:
        axis += (or_dims + 1)
    for i, dim in enumerate(or_shape):
        if i == axis:
            new_shape.append(1)
        new_shape.append(dim)
    if axis == or_dims:
        new_shape.append(1)
    input_to_concatenate = []
    for array in arrays:
        input_to_concatenate.append(reshape.reshape_1(array, new_shape))
    input_to_concatenate = [axis] + input_to_concatenate
    return concatenate.concatenate_1(*input_to_concatenate)

def test_stack():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.stack

    A = jrr(key, (3, 5, 7), 0, 10)
    B = jrr(key, (3, 5, 7), 0, 10)
    D = jrr(key, (), 0, 10)
    E = jrr(key, (), 0, 10)
    C = jrr(key, (1,), 0, 10)

    for arrays, axis in itertools.product(*[((A,B), (A,), (C,), (C,C)), (0, 1, -1)]):
        if arrays[0].ndim == 1 and axis == 1:
            continue
        Alist = [i.tolist() for i in arrays]
        assert(np.array_equal(op(arrays, axis),np.asarray(stack_1(axis, *Alist))))
    for arrays, axis in itertools.product(*[((E, D,),), (0,)]):
        Alist = [i.tolist() for i in arrays]		
        lhs = op(arrays, axis)
        rhs = np.asarray(stack_1(axis, *Alist))
        assert(np.array_equal(lhs,rhs))