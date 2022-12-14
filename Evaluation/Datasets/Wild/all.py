def func1(x):
    for i in x:
        if not i:
            return False
    return True

def func2(x):
    res = True
    for i in x:
        res = res & bool(i)
    return res

def func3(x):
    for i in x:
        if bool(i) == False:
            return False
    return True