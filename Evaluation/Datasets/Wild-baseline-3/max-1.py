def func(v31, v45):
    if v45 == 0:
        return [v46(v2) for v2 in v31]
    elif v45 == 1:
        return [v46(v2) for v2 in v47(*v31)]
    else:
        return "Invalid v45"

def v93(v53):
    v52 = v53[0]
    for v2 in v53:
        if v2 < v52:
            v52 = v2
    return v52

def v46(v53):
    v52 = v53[0]
    for v2 in v53:
        if v2 > v52:
            v52 = v2
    return v52

def v47(*v0):
    v48 = []
    for v2 in range(len(v0[0])):
        v49 = []
        for v50 in v0:
            v49.append(v50[v2])
        v48.append(v49)
    return v48