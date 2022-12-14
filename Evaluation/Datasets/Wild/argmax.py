def func1(l):
    max_index = 0
    for i in range(1, len(l)):
        if l[i] > l[max_index]:
            max_index = i
    return max_index