def func(x):
    y = []
    for i in range(1, len(x)):
        y.append(x[i] - x[i-1])
    return y