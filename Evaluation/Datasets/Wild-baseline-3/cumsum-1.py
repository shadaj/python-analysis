def func(v10):
    v34 = 0

    for v2 in range(len(v10)):
        # Maintaining an accumulator which tracks the sum
        v34 += v10[v2]
        v10[v2] = v34
    return v10