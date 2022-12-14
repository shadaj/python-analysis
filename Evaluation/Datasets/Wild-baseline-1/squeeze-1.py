def func(l):
    if not isinstance(l, list):
        return l
    elif len(l) == 1:
        return func1(l[0])
    else:
        return [func1(i) for i in l]