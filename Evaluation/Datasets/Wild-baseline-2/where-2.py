def func(v10,v11,v12):
    v3 = []
    for v2 in range(len(v10)):
        if v10[v2]:
            v3.append(v11[v2])
        else:
            v3.append(v12[v2])
    return v3