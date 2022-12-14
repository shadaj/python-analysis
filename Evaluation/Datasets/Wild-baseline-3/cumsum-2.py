def func(v10):
    v34 = 0
    v3 = []
    for v2 in range(len(v10)):
        # Maintaining an accumulator which tracks the sum
        v34 += v10[v2]
        # Adding the sum to the result to be returned
        v3.append(v34)
    return v3