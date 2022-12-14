def func1(x):
    for i in x:
        if i:
            return True
    return False

def func2(x):
    res = False
    for i in x:
        res = res | bool(i)
    return res