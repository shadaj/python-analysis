def bubble(a):
    i = 0
    while i < len(a):
        j = i+1
        while j < len(a):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
            j += 1
        i += 1
    return a

def bubble_for(a):
    for i in range(len(a)):
        for j in range(1, len(a) - i):
            if a[j-1] < a[j]:
                a[j-1], a[j] = a[j], a[j-1]
    return a