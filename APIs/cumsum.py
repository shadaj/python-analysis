import shape, zeros, prod
import itertools

def cumsum_1(a, axis=None):
    shape_input = shape.shape_1(a)
    dim_input = len(shape_input)

    if axis is not None:
        if axis < 0:
            axis += dim_input

    shape_accumulator = []
    index_flags = []
    for i in range(dim_input):
        if i == axis:
            index_flags.append(None)
        else:
            shape_accumulator.append(shape_input[i])
            index_flags.append(True)

    accumulator = zeros.zeros_1(shape_accumulator)
    if axis is not None:
        output = zeros.zeros_1(shape_input)
    else:
        output = zeros.zeros_1(prod.prod_1(shape_input))

    counter = 0
    for indices in itertools.product(*[list(range(j)) for j in shape_input]):
        inp = a
        out = accumulator
        prev_out = [out, None]
        for i, index in enumerate(indices):
            inp = inp[index]
            if index_flags[i] == True:
                prev_out = [out, index]
                out = out[index]
        if axis is not None:
            if prev_out[1] is not None:
                prev_out[0][prev_out[1]] += inp
                acc_val = prev_out[0][prev_out[1]]
            else:
                accumulator += inp 	#Reduction results in a singleton value
                acc_val = accumulator
            outp = output
            for i, index in enumerate(indices):
                if i + 1 == len(indices):
                    outp[index] = acc_val
                else:
                    outp = outp[index] 
        else:
            if counter == 0:
                output[counter] = inp
            else:
                output[counter] = output[counter-1] + inp
        counter += 1
            
    return output

def test_cumsum():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (), 0, 10)
    B = jrr(key, (5,), 0, 10)
    C = jrr(key, (2, 5, 3, 4), 0, 10)
    for a, axis in itertools.product(*[(A, B, C), (None, 0, -1)]):
        if len(a.shape) == 0 and axis is not None:
            continue
        else:
            print(a, axis)
            res1 = np.cumsum(a, axis=axis)
            res2 = np.asarray(cumsum_1(a.tolist(), axis=axis))  
            assert(np.allclose(res1, np.asarray(res2)))