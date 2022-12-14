def func(v10,v11,v12):
    for v2 in range(len(v10)):
        if v10[v2]<v11:
            v10[v2]=v11
        elif v10[v2]>v12:
            v10[v2]=v12
    return v10