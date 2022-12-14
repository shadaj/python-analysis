def summation(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

def func1(x):
    return summation(x)

def func2(l):
    sum=0
    for i in l:
        for j in i:
            sum=sum+j
    return sum