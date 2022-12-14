def func(l):
    s = 0
    res = []
    for i in range(len(l)):
        s += l[i]
        res.append(s)
    return res