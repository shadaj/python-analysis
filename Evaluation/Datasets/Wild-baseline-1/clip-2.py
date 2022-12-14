def min(a, b):
    return a if a < b else b

def max(a, b):
    return a if a > b else b

def func(l, a, b):
    return [min(max(x, a), b) for x in l]