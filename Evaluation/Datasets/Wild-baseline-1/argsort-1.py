def sort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i][0] > list[j][0]:
                list[i], list[j] = list[j], list[i]
    return list

def func(seq):
    tupled = [(seq[i], i) for i in range(len(seq))]
    return [i[1] for i in sort(tupled)]