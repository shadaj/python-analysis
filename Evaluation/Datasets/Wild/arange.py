def func1(start, stop, step):
    return [start + step * i for i in range(int((stop - start) / step))]

def func2(start, stop=None, step=1):
    res = []
    if stop is None:
        stop = start
        start = 0
    while start < stop:
        res.append(start)
        start += step
    return res