def matmul(a, b, c):
    I = len(a)
    J = len(b)
    K = len(b[0])

    i = 0
    while i < I:
        j = 0
        while j < J:
            k = 0
            while k < K:
                c[i][k] = c[i][k] + a[i][j] * b[j][k]
                k+=1
            j+=1
        i+=1

def matmul_for(a, b, c):
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(b[j])):
                c[i][k] = c[i][k] + a[i][j] * b[j][k]
    return c

def matmul2(a, b, c):
    I = len(a)
    J = len(b)
    K = len(b[0])
    blockSize = 2
    Ir, Jr, Kr = I // blockSize + 1, J // blockSize + 1, K // blockSize + 1
    i_b = 0
    while i_b < Ir:
        j_b = 0
        while j_b < Jr:
            k_b = 0
            while k_b < Kr:
                i = i_b * Ir
                while i < min((i_b * Ir + Ir, I)):
                    j = j_b * Jr
                    while j < min((j_b * Jr + Jr, J)):
                        k = k_b * Kr
                        while k < min((k_b * Kr + Kr, K)):
                            c[i][k] += a[i][j] * b[j][k]
                            k += 1
                        j += 1
                    i += 1
                k_b += 1
            j_b += 1
        i_b += 1

def matmul2_for(a, b, c):
    I = len(a)
    J = len(b)
    K = len(b[0])
    blockSize = 2
    Ir, Jr, Kr = I // blockSize + 1, J // blockSize + 1, K // blockSize + 1
    for i_b in range(Ir):
        for j_b in range(Jr):
            for k_b in range(Kr):
                for i in range(i_b * Ir, min((i_b * Ir + Ir, I))):
                    for j in range(j_b * Jr, min((j_b * Jr + Jr, J))):
                        for k in range(k_b * Kr, min((k_b * Kr + Kr, K))):
                            c[i][k] += a[i][j] * b[j][k]

def matadd(a, b):
    I = len(a)
    J = len(a[0])
    c = [[0 for j in range(J)] for i in range(I)]
    for i in range(I):
        for j in range(J):
            c[i][j] = a[i][j] + b[i][j]
    return c

def matsub(a, b):
    I = len(a)
    J = len(a[0])
    c = [[0 for j in range(J)] for i in range(I)]
    for i in range(I):
        for j in range(J):
            c[i][j] = a[i][j] - b[i][j]
    return c


def matmul_strassen(a, b):
    I = len(a)
    J = len(b)
    K = len(b[0])
    if I <= 1:
        return [[a[0][0] * b[0][0]]]
    a11 = [[a[i][j] for j in range(0, J//2)] for i in range(0, I//2)]
    a12 = [[a[i][j] for j in range(J//2, J)] for i in range(0, I//2)]
    a21 = [[a[i][j] for j in range(0, J//2)] for i in range(I//2, I)]
    a22 = [[a[i][j] for j in range(J//2, J)] for i in range(I//2, I)]
    b11 = [[b[i][j] for j in range(0, K//2)] for i in range(0, J//2)]
    b12 = [[b[i][j] for j in range(K//2, K)] for i in range(0, J//2)]
    b21 = [[b[i][j] for j in range(0, K//2)] for i in range(J//2, J)]
    b22 = [[b[i][j] for j in range(K//2, K)] for i in range(J//2, J)]
    m1 = matmul_strassen(matadd(a11, a22), matadd(b11, b22))
    m2 = matmul_strassen(matadd(a21, a22), b11)
    m3 = matmul_strassen(a11, matsub(b12, b22))
    m4 = matmul_strassen(a22, matsub(b21, b11))
    m5 = matmul_strassen(matadd(a11, a12), b22)
    m6 = matmul_strassen(matsub(a21, a11), matadd(b11, b12))
    m7 = matmul_strassen(matsub(a12, a22), matadd(b21, b22))
    c = [[0 for j in range(K)] for i in range(I)]
    for i in range(I//2):
        for k in range(K//2):
            c[i][k]               = m1[i][k] + m4[i][k] - m5[i][k] + m7[i][k]
            c[i][k + K//2]        = m3[i][k] + m5[i][k]
            c[i + I//2][k]        = m2[i][k] + m4[i][k]
            c[i + I//2][k + K//2] = m1[i][k] - m2[i][k] + m3[i][k] + m6[i][k]
    return c

def matmul_recursive(a, b):
    I = len(a)
    J = len(b)
    K = len(b[0])
    if I <= 1:
        return [[a[0][0] * b[0][0]]]
    a11 = [[a[i][j] for j in range(0, J//2)] for i in range(0, I//2)]
    a12 = [[a[i][j] for j in range(J//2, J)] for i in range(0, I//2)]
    a21 = [[a[i][j] for j in range(0, J//2)] for i in range(I//2, I)]
    a22 = [[a[i][j] for j in range(J//2, J)] for i in range(I//2, I)]
    b11 = [[b[i][j] for j in range(0, K//2)] for i in range(0, J//2)]
    b12 = [[b[i][j] for j in range(K//2, K)] for i in range(0, J//2)]
    b21 = [[b[i][j] for j in range(0, K//2)] for i in range(J//2, J)]
    b22 = [[b[i][j] for j in range(K//2, K)] for i in range(J//2, J)]
    m1 = matmul_recursive(a11, b11)
    m2 = matmul_recursive(a12, b21)
    m3 = matmul_recursive(a11, b12)
    m4 = matmul_recursive(a12, b22)
    m5 = matmul_recursive(a21, b11)
    m6 = matmul_recursive(a22, b21)
    m7 = matmul_recursive(a21, b12)
    m8 = matmul_recursive(a22, b22)
    c = [[0 for j in range(K)] for i in range(I)]
    for i in range(I//2):
        for k in range(K//2):
            c[i][k]               = m1[i][k] + m2[i][k]
            c[i][k + K//2]        = m3[i][k] + m4[i][k]
            c[i + I//2][k]        = m5[i][k] + m6[i][k]
            c[i + I//2][k + K//2] = m7[i][k] + m8[i][k]
    return c