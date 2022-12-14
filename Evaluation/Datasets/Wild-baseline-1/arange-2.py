def func(start, stop=None, step=1):
    res = []
    if stop is None:
        stop = start
        start = 0
    while start < stop:
        res.append(start)
        start += step
    return res