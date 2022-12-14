def func(v4, v0, v1):
    v3 = []
    for v2 in range(len(v4)):

        v3.append(v91(v4[v2], v0[v2], v1[v2]))
    return v3

def v91(v90, v0, v1):
    # Can be used as a 2-way multiplexer
    if v90:
        return v0
    else:
        return v1