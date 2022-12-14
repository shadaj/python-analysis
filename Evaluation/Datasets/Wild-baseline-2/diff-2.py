def func(v0):
    v1 = []
    for v2 in range(1, len(v0)):
        v1.append(v0[v2] - v0[v2-1])
    return v1