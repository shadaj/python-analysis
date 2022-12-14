def myzip(*x):
    zipper = []
    for i in range(len(x[0])):
        row = []
        for el in x:
            row.append(el[i])
        zipper.append(row)
    return zipper

def func(lst, axis):
    if axis == 0:
        return [func1(i) for i in lst]
    elif axis == 1:
        return [func1(i) for i in myzip(*lst)]
    else:
        return "Invalid axis"