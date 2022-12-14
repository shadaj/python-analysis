def func(x):
    res = False
    for i in x:
        res = res | bool(i)
    return res