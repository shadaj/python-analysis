def func1(lst):
    count = 0
    for i in lst:
        if i != 0:
            count += 1
    return count

def func2(lst):
    count_row = 0
    count_col = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] != 0:
                count_row += 1
    for i in range(len(lst[0])):
        for j in range(len(lst)):
            if lst[j][i] != 0:
                count_col += 1
    return count_row

def func3(lst):
    count_row = 0
    count_col = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] != 0:
                count_row += 1
    for i in range(len(lst[0])):
        for j in range(len(lst)):
            if lst[j][i] != 0:
                count_col += 1
    return count_col