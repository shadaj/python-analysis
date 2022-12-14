def func(v5, v6, v14=1e-05, v15=1e-08):
    # If the lengths of the inputs is different, the result cannot be True
    if len(v5) != len(v6):
        return False
    for v2 in range(len(v5)):
        if v26(v5[v2] - v6[v2]) > v15 + v14 * v26(v6[v2]):
            return False
    return True

def v26(v0):
    return v0 if v0 > 0 else -v0