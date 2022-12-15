import shape, zeros_like
import itertools

def clip_1(X, xmin, xmax):
    shape_input = shape.shape_1(X)
    output = zeros_like.zeros_like_1(X)

    for indices in itertools.product(*[list(range(j)) for j in shape_input]):
        x = X
        for index in indices:
            x = x[index]
        out = output
        for i, index in enumerate(indices):
            if i + 1 == len(indices):
                if x > xmax:
                    out[index] = xmax
                elif x < xmin:
                    out[index] = xmin
                else:
                    out[index] = x
            else:
                out = out[index]
    if len(shape_input) == 0: 	# Not an array
        if X > xmax:
            return xmax
        elif X < xmin:
            return xmin
        else:
            return X

    return output

def test_abs():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.uniform
    for i in range(10):
        A = jrr(key, (), minval=-5, maxval=5)
        print(A)
        res1 = np.clip(A, -2, 2)
        res2 = np.asarray(clip_1(A.tolist(), -2, 2))
        assert(np.allclose(res1, res2, equal_nan=True))
        A = jrr(key, (2, 6), minval=-5, maxval=5)
        res1 = np.clip(A, -2, 2)
        res2 = np.asarray(clip_1(A.tolist(), -2, 2))
        assert(np.allclose(res1, res2, equal_nan=True))