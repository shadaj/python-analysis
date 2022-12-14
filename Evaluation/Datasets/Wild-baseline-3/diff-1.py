def func(v0):
    # A similar expression can be used to compute gradients of a linear list
    return [v0[v2+1]-v0[v2] for v2 in range(len(v0)-1)]