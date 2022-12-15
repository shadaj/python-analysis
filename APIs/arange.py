def arange_1(start,stop=None,step=None):
    if stop is None:
        stop = start
        start = 0
        if step is None:
            step = 1
    elif step is None:
        step = 1
    assert step != 0
    l=[]
    while True:
        if step < 0 and start <= stop:
            break
        elif step > 0 and start >= stop:
            break
        l.append(start)
        start+=step
    return l

def test_arange():
    import jax
    import jax.numpy as np
    key = jax.random.PRNGKey(2022)
    assert np.array_equal(np.arange(5), np.asarray(arange_1(5)))
    assert np.array_equal(np.arange(5,9), np.asarray(arange_1(5,9)))
    assert np.array_equal(np.arange(5,3), np.asarray(arange_1(5,3)))
    assert np.array_equal(np.arange(5,1,-1), np.asarray(arange_1(5,1,-1)))
    assert np.array_equal(np.arange(5,20,2), np.asarray(arange_1(5,20,2)))
