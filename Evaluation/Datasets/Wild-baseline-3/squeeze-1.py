def func(v10):
    if not isinstance(v10, list):
        return v10
    # If the input is atleast 1D then perform the following
    elif len(v10) == 1:
        return func(v10[0])
    else:
        return [func(v2) for v2 in v10]