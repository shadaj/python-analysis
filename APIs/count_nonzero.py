import shape, zeros
import itertools

def count_nonzero_1(a, axis=None, keepdims=None):
    shape_input = shape.shape_1(a)
    dim_input = len(shape_input)

    if axis is None:
        axis = [i for i in range(dim_input)]
    elif isinstance(axis, int):
        axis = [axis]
    axis = list(axis)
    for i in range(len(axis)):
        if axis[i] < 0:
            axis[i] += dim_input

    new_shape_input = shape.shape_1(a)
    new_dim_input = len(new_shape_input)

    shape_output = []
    index_flags = []
    for i_raw in range(new_dim_input):
        if i_raw < new_dim_input - dim_input:
            index_flags.append(None)
        else:
            i = i_raw - (new_dim_input - dim_input)
            if i in axis:
                if keepdims:
                    shape_output.append(1)
                    index_flags.append(False)
                else:
                    index_flags.append(None)
            else:
                if shape_input[i] == new_shape_input[i_raw]:
                    shape_output.append(shape_input[i])
                    index_flags.append(True)
                else:
                    shape_output.append(1)
                    index_flags.append(False)

    output = zeros.zeros_1(shape_output)

    for indices in itertools.product(*[list(range(j)) for j in new_shape_input]):
        inp = a
        out = output
        prev_out = [out, None]
        for i, index in enumerate(indices):
            inp = inp[index]
            if index_flags[i] == True:
                prev_out = [out, index]
                out = out[index]
            elif index_flags[i] == False:
                prev_out = [out, 0]
                out = out[0]
        if prev_out[1] is not None:
            if inp != 0:
                prev_out[0][prev_out[1]] += 1
        else:
            if inp != 0:
                output += 1 	#Reduction results in a singleton value
            
    return output

def test_count_nonzero():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (2, 5, 3, 4), 0, 2)
    B = jrr(key, (6,), 0, 2)
    C = jrr(key, (), 0, 2)
    for a, axis, keepdims in itertools.product(*[(A, B, C), (None, 0, -1, (0,-1)), (True, False)]):
        if len(a.shape) == 0 and axis is not None:
            continue
        if len(a.shape) == 1 and axis == (0, -1):
            continue
        res1 = np.count_nonzero(a, axis=axis, keepdims=keepdims)
        res2 = np.asarray(count_nonzero_1(a.tolist(), axis=axis, keepdims=keepdims))  
        assert(np.allclose(res1, np.asarray(res2)))