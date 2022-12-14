def func(a,b):
    if len(a[0]) != len(b):
        return "Invalid input"
    else:
        result = []
        for i in range(len(a)):
            row = []
            for j in range(len(b[0])):
                sum = 0
                for k in range(len(b)):
                    sum += a[i][k] * b[k][j]
                row.append(sum)
            result.append(row)
        return result