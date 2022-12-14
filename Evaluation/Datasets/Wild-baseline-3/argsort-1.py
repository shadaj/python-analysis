def func(v24):
    v23 = [(v24[v2], v2) for v2 in range(len(v24))]
    return [v2[1] for v2 in v25(v23)]

def v25(v27):
    for v2 in range(len(v27)):
        for v8 in range(v2+1, len(v27)):
            if v27[v2][0] > v27[v8][0]:
                v27[v2], v27[v8] = v27[v8], v27[v2]
    return v27