def v86(*v0):
    v87 = []
    for v2 in range(len(v0[0])):
        v88 = []
        for v50 in v0:
            v88.append(v50[v2])
        v87.append(v88)
    return v87


def func(v10):
    return v86(*v10)