def v28(v11, v12):
    return v11 if v11 < v12 else v12

def v29(v11, v12):
    return v11 if v11 > v12 else v12

def func(v10, v11, v12):
    return [v28(v29(v0, v11), v12) for v0 in v10]