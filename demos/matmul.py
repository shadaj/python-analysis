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
