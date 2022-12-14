def func(l,a,b):
    res = []
    for i in range(len(l)):
        if l[i]:
            res.append(a[i])
        else:
            res.append(b[i])
    return res