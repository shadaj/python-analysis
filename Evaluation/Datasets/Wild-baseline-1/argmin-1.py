def func(l):
    min_index = 0
    for i in range(1, len(l)):
        if l[i] < l[min_index]:
            min_index = i
    return min_index