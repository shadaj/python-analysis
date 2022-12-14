def func1(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

def func2(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    pivot = a[len(a) // 2]
    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return func2(smaller) + equal + func2(larger)