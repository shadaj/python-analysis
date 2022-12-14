def func(v18, v19, v20):
    # Using list comprehension to generate a list of all the elements which are a part of the series
    return [v18 + v20 * v2 for v2 in range(int((v19 - v18) / v20))]