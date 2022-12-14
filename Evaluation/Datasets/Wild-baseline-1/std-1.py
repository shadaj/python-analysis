def summation(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

def length(list):
    i = 0
    for l in list:
        i += 1
    return i

def func(x):
    n = length(x)
    mean = summation(x)/n
    return (summation([(i-mean)**2 for i in x])/n)**0.5