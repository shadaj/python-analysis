def func1(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
        l[i] = s
    return l

def func2(l):
    s = 0
    res = []
    for i in range(len(l)):
        s += l[i]
        res.append(s)
    return res