def length(list):
    i = 0
    for l in list:
        i += 1
    return i

def func(list):
    sum = 0
    for i in list:
        sum += i
    return sum/length(list)