def func(v11):
    if len(v11) <= 1:
        return v11
    v73, v74, v75 = [], [], []
    v72 = v11[len(v11) // 2]
    for v0 in v11:
        if v0 < v72:
            v73.append(v0)
        elif v0 == v72:
            v74.append(v0)
        else:
            v75.append(v0)
    return func2(v73) + v74 + func2(v75)