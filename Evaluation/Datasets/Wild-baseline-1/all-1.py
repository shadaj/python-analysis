def func(x):
    res = True
    for i in x:
        res = res & bool(i)
    return res