def func(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min