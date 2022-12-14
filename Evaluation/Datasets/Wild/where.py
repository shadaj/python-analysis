def where(condition, x, y):
    if condition:
        return x
    else:
        return y

def func1(c, x, y):
    res = []
    for i in range(len(c)):
        res.append(where(c[i], x[i], y[i]))
    return res

def func2(l,a,b):
    res = []
    for i in range(len(l)):
        if l[i]:
            res.append(a[i])
        else:
            res.append(b[i])
    return res