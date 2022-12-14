def func(v68):
    v67 = []
    for v2 in v68:
        if type(v2) == list:
            for v8 in v2:
                v67.append(v8)
        else:
            v67.append(v2)
    return v67