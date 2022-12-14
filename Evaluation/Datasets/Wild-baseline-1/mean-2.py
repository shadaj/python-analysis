def func(l):
    sum=0
    count=0
    for i in l:
        for j in i:
            sum=sum+j
            count=count+1
    return sum/count