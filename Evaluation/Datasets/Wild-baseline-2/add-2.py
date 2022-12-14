def func(v5, v6):
    if len(v5) != len(v6):
        return None
    else:
        v13 = []
        for v2 in range(len(v5)):
            if len(v5[v2]) != len(v6[v2]):
                return None
            else:
                v13.append([])
                for v8 in range(len(v5[v2])):
                    v13[v2].append(v5[v2][v8] + v6[v2][v8])
        return v13