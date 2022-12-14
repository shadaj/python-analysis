def func(v31):
    v32 = 0
    v33 = 0
    for v2 in range(len(v31)):
        for v8 in range(len(v31[v2])):
            if v31[v2][v8] != 0:
                v32 += 1
    for v2 in range(len(v31[0])):
        for v8 in range(len(v31)):
            if v31[v8][v2] != 0:
                v33 += 1
    return v33