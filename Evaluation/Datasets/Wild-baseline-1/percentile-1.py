def sort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

def func(x,p):
    x = sort(x)
    n = len(x)
    if p < 0 or p > 100:
        raise ValueError("Percentile must be between 0 and 100")
    elif p == 0:
        return x[0]
    elif p == 100:
        return x[-1]
    else:
        i = (n-1)*p/100
        f = int(i)
        c = int(i) + 1
        if f == i:
            return x[int(i)]
        else:
            return x[int(f)]*(c-i) + x[int(c)]*(i-f)