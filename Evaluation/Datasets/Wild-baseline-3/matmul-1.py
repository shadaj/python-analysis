def func(v11,v12):
    if len(v11[0]) != len(v12):
        return "Invalid input"
    else:
        v43 = []
        for v2 in range(len(v11)):
            v44 = []
            for v8 in range(len(v12[0])):
                v92 = 0
                for v9 in range(len(v12)):
                    v92 += v11[v2][v9] * v12[v9][v8]
                v44.append(v92)
            v43.append(v44)
        return v43