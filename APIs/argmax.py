import shape, ones, add, ones_like, mul, zeros_like, ravel
import itertools


def argmax_1(a, axis=None, keepdims=None):
    shape_input = shape.shape_1(a)
    dim_input = len(shape_input)

    if axis is None:
        a = ravel.ravel_1(a)
        axis = 0
        shape_input = shape.shape_1(a)
        dim_input = len(shape_input)
    else:
        if axis < 0:
            axis += dim_input

    shape_output = []
    index_flags = []
    for i in range(dim_input):
        if i == axis:
            if keepdims:
                shape_output.append(1)
                index_flags.append(False)
            else:
                index_flags.append(None)
        else:
            shape_output.append(shape_input[i])
            index_flags.append(True)

    output = ones.ones_1(shape_output)
    indices_ret = zeros_like.zeros_like_1(output)
    output = mul.mul_1(output, -float("inf"))

    for indices in itertools.product(*[list(range(j)) for j in shape_input]):
        inp = a
        out = output
        outindex = indices_ret
        prev_out = [out, None]
        prev_outindex = [outindex, None]
        argindex = None
        for i, index in enumerate(indices):
            inp = inp[index]
            if index_flags[i] == True:
                prev_out = [out, index]
                prev_outindex = [outindex, index]
                out = out[index]
                outindex = outindex[index]
            elif index_flags[i] == False:
                prev_out = [out, 0]
                out = out[0]
                prev_outindex = [outindex, 0]
                outindex = outindex[0]
            if i == axis:
                argindex = index
        if prev_out[1] is not None:
            if inp > prev_out[0][prev_out[1]]:
                prev_out[0][prev_out[1]] = inp
                prev_outindex[0][prev_outindex[1]] = argindex
        else:
            if inp > output:
                output = inp 	#Reduction results in a singleton value
                indices_ret = argindex
                
    return indices_ret

def test_argmax():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (2, 5, 3, 4), -10, 10)
    for a, axis, keepdims in itertools.product(*[(A), (None, 1, -1, 0), (True, False)]):
        try:
            res1 = np.argmax(a, axis=axis, keepdims=keepdims)
        except:
            continue
        res2 = np.asarray(argmax_1(a.tolist(), axis=axis, keepdims=keepdims))  

        assert(np.allclose(res1, np.asarray(res2)))