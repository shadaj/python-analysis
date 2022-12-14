def summation(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

def func1(x,y):
    return summation([x[i]*y[i] for i in range(len(x))])