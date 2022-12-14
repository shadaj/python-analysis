def sort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

def func1(x):
    x = sort(x)
    n = len(x)
    if n % 2 == 0:
        return (x[n//2] + x[n//2-1])/2
    else:
        return x[n//2]