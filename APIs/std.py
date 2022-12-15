import mean, mul, sqrt, sub, pow
import itertools

def std_1(a, axis=None, keepdims=None, where=None):
    mn = mean.mean_1(a, axis, True, where)
    return sqrt.sqrt_1(mean.mean_1(pow.pow_1(sub.sub_1(a, mn), 2), axis, keepdims, where))

def std_2(a, axis=None, keepdims=None, where=None):
    mn = mean.mean_1(a, axis, keepdims, where)
    mn2 = mean.mean_1(mul.mul_1(a, a), axis, keepdims, where)
    return sqrt.sqrt_1(sub.sub_1(mn2, mul.mul_1(mn, mn)))

def test_std():
    import jax as jax
    import jax.numpy as np
    import operator
    key = jax.random.PRNGKey(2022)
    jrr = jax.random.randint
    A = jrr(key, (2, 5, 3, 4), 0, 10)
    whr = jrr(key, (5,1,4), 0, 2)
    for a, axis, keepdims, where in itertools.product(*[(A), (None, 1, -1, [0,-1]), (True, False), (None, whr)]):
        res1 = np.std(A, axis=axis, keepdims=keepdims, where=where)
        wherel = where.tolist() if where is not None else None
        res2 = np.asarray(std_1(A.tolist(), axis=axis, keepdims=keepdims, where=wherel))
        assert(np.allclose(res1, np.asarray(res2), equal_nan=True))
    for a, axis, keepdims, where in itertools.product(*[(A), (None, 1, -1, [0,-1]), (True, False), (None, whr)]):
        res1 = np.std(A, axis=axis, keepdims=keepdims, where=where)
        wherel = where.tolist() if where is not None else None
        res2 = np.asarray(std_2(A.tolist(), axis=axis, keepdims=keepdims, where=wherel))
        assert(np.allclose(res1, np.asarray(res2), equal_nan=True))