def length(list):
    i = 0
    for l in list:
        i += 1
    return i

def func1(list):
    sum = 0
    for i in list:
        sum += i
    return sum/length(list)

def func2(l):
    sum=0
    count=0
    for i in l:
        for j in i:
            sum=sum+j
            count=count+1
    return sum/count