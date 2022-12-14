def func1(l,a,b):
    for i in range(len(l)):
        if l[i]<a:
            l[i]=a
        elif l[i]>b:
            l[i]=b
    return l

def min(a, b):
    return a if a < b else b

def max(a, b):
    return a if a > b else b

def func2(l, a, b):
    return [min(max(x, a), b) for x in l]