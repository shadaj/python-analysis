def func1(x,y):
    return [x[i]+y[i] for i in range(len(x))]

def func2(list1, list2):
    if len(list1) != len(list2):
        return None
    else:
        new_list = []
        for i in range(len(list1)):
            if len(list1[i]) != len(list2[i]):
                return None
            else:
                new_list.append([])
                for j in range(len(list1[i])):
                    new_list[i].append(list1[i][j] + list2[i][j])
        return new_list