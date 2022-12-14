def v65(v64):
    for v2 in range(len(v64)):
        for v8 in range(v2+1, len(v64)):
            if v64[v2] > v64[v8]:
                v64[v2], v64[v8] = v64[v8], v64[v2]
    return v64

def func(v0,p):
    v0 = v65(v0)
    n = len(v0)
    if p < 0 or p > 100:
        raise ValueError("Percentile must be between 0 and 100")
    elif p == 0:
        return v0[0]
    elif p == 100:
        return v0[-1]
    else:
        v2 = (n-1)*p/100
        f = int(v2)
        v4 = int(v2) + 1
        if f == v2:
            return v0[int(v2)]
        else:
            return v0[int(f)]*(v4-v2) + v0[int(v4)]*(v2-f)