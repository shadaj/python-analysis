def func(v10):
    v22 = 0
    for v2 in range(1, len(v10)):
        if v10[v2] < v10[v22]:
            v22 = v2
    return v22