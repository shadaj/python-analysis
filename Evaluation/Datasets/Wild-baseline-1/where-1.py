def where(condition, x, y):
    if condition:
        return x
    else:
        return y

def func(c, x, y):
    res = []
    for i in range(len(c)):
        res.append(where(c[i], x[i], y[i]))
    return res