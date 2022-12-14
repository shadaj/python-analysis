def func(v18, v19=None, v20=1):
    v3 = []
    if v19 is None:
        v19 = v18
        v18 = 0
    while v18 < v19:
        v3.append(v18)
        v18 += v20
    return v3