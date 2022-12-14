def func1(l):
    p=1
    for i in l:
        p=p*i
    return p


def func2(l):
    mul=1
    for i in l:
        for j in i:
            mul=mul*j
    return mul