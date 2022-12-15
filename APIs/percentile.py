import shape, transpose, reshape, sort, zeros
import itertools

def percentile_1(a, q, axis=None, keepdims=False):
    shape_inp = shape.shape_1(a)
    dim_inp = len(shape_inp)
    if axis is None:
        axis = [i for i in range(dim_inp)]
    if isinstance(axis, int):
        axis = [axis]
    for i in range(len(axis)):
        if axis[i] < 0:
            axis[i] += dim_inp

    transpose_axis = []
    reshape_shape = []
    keepdim_shape = []
    for i in range(dim_inp):
        if i not in axis:
            transpose_axis.append(i)
            reshape_shape.append(shape_inp[i])
            keepdim_shape.append(shape_inp[i])
        else:
            keepdim_shape.append(1)
    for i in range(dim_inp):
        if i in axis:
            transpose_axis.append(i)
    reshape_shape.append(-1)

    a = transpose.transpose_1(a, transpose_axis)
    a = reshape.reshape_1(a, reshape_shape)
    num_el = shape.shape_1(a)[-1]
    if keepdims:
        reshape_shape[-1] = 1
    else:
        reshape_shape.pop()

    output = zeros.zeros_1(reshape_shape)
    a_sort = sort.sort_1(a, -1)

    ind = (q * (num_el-1)) / 100
    for indices in itertools.product(*[list(range(j)) for j in reshape_shape]):
        a = a_sort
        if keepdims:
            for index in indices[:-1]:
                a = a[index]
        else:
            for index in indices:
                a = a[index]

        out = output
        for i, index in enumerate(indices):
            if i + 1 == len(indices):
                
                if int(ind) == ind:
                    out[index] = a[int(ind)]
                else:
                    ind1 = int(ind)
                    ind2 = ind1 + 1
                    w1 = ind2 - ind
                    w2 = ind - ind1
                    out[index] = w1 * a[ind1] + w2 * a[ind2]
            else:
                out = out[index]

    if reshape_shape == []:
        if int(ind) == ind:
            return a_sort[int(ind)]
        else:
            ind1 = int(ind)
            ind2 = ind1 + 1
            w1 = ind2 - ind
            w2 = ind - ind1
            return w1 * a_sort[ind1] + w2 * a_sort[ind2]

    if keepdims:
        return reshape.reshape_1(output, keepdim_shape)

    return output

def test_percentile():
    import numpy as np

    for percentile in [0, 25, 50, 75, 100]:
        for keepdims in [False, True]:
            A = np.random.randint(-10, 10, size=(1,))
            assert(np.percentile(A, percentile, axis = 0, keepdims=keepdims).tolist() == percentile_1(A.tolist(), percentile, axis=0, keepdims=keepdims))

        for keepdims in [False, True]:
            A = np.random.randint(-10, 10, size=(5,))
            assert(np.percentile(A, percentile, axis = 0, keepdims=keepdims).tolist() == percentile_1(A.tolist(), percentile, axis=0, keepdims=keepdims))


        for keepdims in [False, True]:
            A = np.random.randint(-10, 10, size=(6,))
            assert(np.percentile(A, percentile, axis = 0, keepdims=keepdims).tolist() == percentile_1(A.tolist(), percentile, axis=0, keepdims=keepdims))


        for keepdims in [False, True]:
            A = np.random.randint(-10, 10, size=(3, 4))
            assert(np.percentile(A, percentile, axis = 0, keepdims=keepdims).tolist() == percentile_1(A.tolist(), percentile, axis=0, keepdims=keepdims))


        for keepdims in [False, True]:
            A = np.random.randint(-10, 10, size=(3, 4))
            assert(np.percentile(A, percentile, axis = -1, keepdims=keepdims).tolist() == percentile_1(A.tolist(), percentile, axis=-1, keepdims=keepdims))


        for keepdims in [False, True]:
            A = np.random.randint(-10, 10, size=(3, 4, 5, 6))
            assert(np.percentile(A, percentile, axis = [1, -1], keepdims=keepdims).tolist() == percentile_1(A.tolist(), percentile, axis=[1,-1], keepdims=keepdims))


        for keepdims in [False, True]:
            A = np.random.randint(-10, 10, size=(3, 4, 5, 6))
            assert(np.percentile(A, percentile, axis = None, keepdims=keepdims).tolist() == percentile_1(A.tolist(), percentile, axis=None, keepdims=keepdims))


        