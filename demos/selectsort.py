def selection_sort(a):
    for i in range(len(a)):
        maxv = a[i]
        maxi = i 
        for j in range(i+1, len(a)):
            maxi = j if a[j] < maxv else maxi
            maxv = a[j] if a[j] < maxv else maxv
        a[i], a[maxi] = a[maxi], a[i]
    return a