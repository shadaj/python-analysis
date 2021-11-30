def bubble(a):
    i = 0
    while i < len(a):
        j = i+1
        while j < len(a):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
            j += 1
        i += 1