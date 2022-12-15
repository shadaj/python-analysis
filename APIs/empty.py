def empty_1(shape):
    if isinstance(shape, int):
        return [0] * shape
    elif len(shape) == 0:
        return 0
    else:
        return [empty_1(shape[1:]) for i in range(shape[0])]