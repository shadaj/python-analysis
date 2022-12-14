def func(arr):
    new_arr = []
    for i in arr:
        if type(i) == list:
            for j in i:
                new_arr.append(j)
        else:
            new_arr.append(i)
    return new_arr