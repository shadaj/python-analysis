def func(start, stop, step):
    return [start + step * i for i in range(int((stop - start) / step))]