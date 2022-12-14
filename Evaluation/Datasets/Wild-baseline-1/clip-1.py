def func(l,a,b):
    for i in range(len(l)):
        if l[i]<a:
            l[i]=a
        elif l[i]>b:
            l[i]=b
    return l