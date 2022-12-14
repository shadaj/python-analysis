def func(list1,index,element):
    list1.append(0)
    for i in range(len(list1)-1,index,-1):
        list1[i]=list1[i-1]
    list1[index]=element
    return list1