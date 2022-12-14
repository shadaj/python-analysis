def func1(x):
    return [x[i+1]-x[i] for i in range(len(x)-1)]

def func2(x):
    y = []
    for i in range(1, len(x)):
        y.append(x[i] - x[i-1])
    return y