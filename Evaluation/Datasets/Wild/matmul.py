def func1(a,b):
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

def func2(A,B):
    C = [[[0 for i in range(len(A[0][0]))] for j in range(len(A[0]))] for k in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0][0])):
                for l in range(len(A[0][0])):
                    C[i][j][k] = A[i][j][l] * B[i][l][k]
    return C