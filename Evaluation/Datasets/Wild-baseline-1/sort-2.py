def func(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    pivot = a[len(a) // 2]
    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return func2(smaller) + equal + func2(larger)