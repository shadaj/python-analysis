def absolute(x):
    return x if x > 0 else -x

def func1(list1, list2, rtol=1e-05, atol=1e-08):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if absolute(list1[i] - list2[i]) > atol + rtol * absolute(list2[i]):
            return False
    return True