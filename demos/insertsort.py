def insertion_sort(a):
    for i in range(1, len(a)):
        j = i - 1
        t = a[i]
        while j >= 0:
            if a[j] > t:
                a[j + 1] = a[j]
            else:
                break
            j -= 1
        a[j+1] = t
    return a
            