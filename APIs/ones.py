def ones_1(shape):
    if isinstance(shape, int):
        return [1] * shape
    elif len(shape) == 0:
        return 1
    else:
        return [ones_1(shape[1:]) for i in range(shape[0])]