def func1(l):
    return [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]

def myzip(*x):
    zipper = []
    for i in range(len(x[0])):
        row = []
        for el in x:
            row.append(el[i])
        zipper.append(row)
    return zipper


def func2(l):
    return myzip(*l)
    #return list(map(list, zip(*l)))

def func3(l):
    return list(map(list, zip(*l)))