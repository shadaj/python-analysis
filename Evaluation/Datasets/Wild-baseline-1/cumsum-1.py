def func(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
        l[i] = s
    return l