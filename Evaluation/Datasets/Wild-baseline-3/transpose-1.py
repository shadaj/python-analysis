def func(v10):
    return v86(*v10)

def v86(*v0):
    v87 = []
    # Iterating across first two dimensions and moving the axes
    for v2 in range(len(v0[0])):
        v88 = []
        for v50 in v0:
            v88.append(v50[v2])
        v87.append(v88)
    return v87