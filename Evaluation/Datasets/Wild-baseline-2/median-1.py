def v57(v56):
    for v2 in range(len(v56)):
        for v8 in range(v2+1, len(v56)):
            if v56[v2] > v56[v8]:
                v56[v2], v56[v8] = v56[v8], v56[v2]
    return v56

def func(v0):
    v0 = v57(v0)
    v58 = len(v0)
    if v58 % 2 == 0:
        return (v0[v58//2] + v0[v58//2-1])/2
    else:
        return v0[v58//2]