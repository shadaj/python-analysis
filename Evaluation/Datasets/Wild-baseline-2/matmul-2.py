def func(v11,v12):
    v4 = [[[0 for v2 in range(len(v11[0][0]))] for v8 in range(len(v11[0]))] for v9 in range(len(v11))]
    for v2 in range(len(v11)):
        for v8 in range(len(v11[0])):
            for v9 in range(len(v11[0][0])):
                for v10 in range(len(v11[0][0])):
                    v4[v2][v8][v9] = v11[v2][v8][v10] * v12[v2][v10][v9]
    return v4