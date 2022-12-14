def myzip(*x):
    zipper = []
    for i in range(len(x[0])):
        row = []
        for el in x:
            row.append(el[i])
        zipper.append(row)
    return zipper


def func(l):
    return myzip(*l)