def func(v10):
    if not isinstance(v10, list):
        return v10
    elif len(v10) == 1:
        return func(v10[0])
    else:
        return [func(v2) for v2 in v10]