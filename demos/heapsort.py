def trickleDown(a, i, length):
    current = i
    if 2*i+2 >= length:
        if 2*i+1 >= length:
            return
        else:
            child = 2*i+1
    else:
        if a[2*i+1] > a[2*i+2]:
            child = 2*i+1
        else:
            child = 2*i+2
    if a[current] >= a[child]:
        return
    else:
        a[current], a[child] = a[child], a[current]
        trickleDown(a, child, length)

def heapify(a):
    i = len(a) - 1
    while i >= 0:
        trickleDown(a, i, len(a))
        i-=1 


def heapsort(a):
    heapify(a)
    heapLength = len(a)
    i = 0
    while i < len(a):
        a[0], a[heapLength-1] = a[heapLength-1], a[0]
        heapLength -=1
        trickleDown(a, 0, heapLength)
        i+=1
    return a