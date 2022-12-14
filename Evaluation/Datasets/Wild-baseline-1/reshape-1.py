def func(lst, shape):
    if len(lst) != shape[0]*shape[1]:
        return None
    else:
        return [lst[i:i+shape[1]] for i in range(0, len(lst), shape[1])]