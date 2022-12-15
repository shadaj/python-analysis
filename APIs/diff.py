import shape, zeros, util
import itertools

def diff_1(a, n=1, axis=-1):
    if n == 0:
        return a
    shape_input = shape.shape_1(a)
    dim_input = len(shape_input)

    if axis < 0:
        axis += dim_input

    shape_accumulator = []
    index_flags = []
    shape_output = []
    for i in range(dim_input):
        if i == axis:
            index_flags.append(None)
            shape_output.append(shape_input[i] - 1)
        else:
            shape_accumulator.append(shape_input[i])
            index_flags.append(True)
            shape_output.append(shape_input[i])

    accumulator = util.nones(shape_accumulator)
    output = zeros.zeros_1(shape_output)

    for indices in itertools.product(*[list(range(j)) for j in shape_input]):
        inp = a
        out = accumulator
        prev_out = [out, None]
        for i, index in enumerate(indices):
            inp = inp[index]
            if index_flags[i] == True:
                prev_out = [out, index]
                out = out[index]
        if out is not None:
            cur_diff = inp - out
            if prev_out[1] is not None:
                prev_out[0][prev_out[1]] = inp
            else:
                accumulator = inp 	#Reduction results in a singleton value
            outp = output
            for i, index in enumerate(indices):
                if i == axis:
                    index -= 1
                if i + 1 == len(indices):
                    outp[index] = cur_diff
                else:
                    outp = outp[index]
        else:
            if prev_out[1] is not None:
                prev_out[0][prev_out[1]] = inp
            else:
                accumulator = inp 	#Reduction results in a singleton value
            
    return diff_1(output, n-1, axis)

def test_diff():
    import jax as jax
    import jax.numpy as np
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    op = np.diff

    for n in range(1,3):
        A = jrr(key, (3, 4, 5), 0, 5)
        n = 1
        axis = -1
        assert(op(A, n, axis).tolist() == diff_1(A.tolist(), n, axis))

        A = jrr(key, (3,), 0, 5)
        n = 1
        axis = -1
        assert(op(A, n, axis).tolist() == diff_1(A.tolist(), n, axis))

        A = jrr(key, (3,4, 5), 0, 5)
        n = 1
        axis = 2
        assert(op(A, n, axis).tolist() == diff_1(A.tolist(), n, axis))

        A = jrr(key, (1,), 0, 5)
        n = 1
        axis = -1
        assert(op(A, n, axis).tolist() == diff_1(A.tolist(), n, axis))

        A = jrr(key, (1,1), 0, 5)
        n = 1
        axis = -1
        assert(op(A, n, axis).tolist() == diff_1(A.tolist(), n, axis))
