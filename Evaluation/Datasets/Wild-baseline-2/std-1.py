def v76(v77):
    v78 = 0
    for v2 in v77:
        v78 = v78 + v2
    return v78

def v79(v77):
    v2 = 0
    for v10 in v77:
        v2 += 1
    return v2

def func(v0):
    v81 = v79(v0)
    v80 = v76(v0)/v81
    return (v76([(v2-v80)**2 for v2 in v0])/v81)**0.5