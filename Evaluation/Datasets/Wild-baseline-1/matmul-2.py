def func(A,B):
    C = [[[0 for i in range(len(A[0][0]))] for j in range(len(A[0]))] for k in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A[0][0])):
                for l in range(len(A[0][0])):
                    C[i][j][k] = A[i][j][l] * B[i][l][k]
    return C