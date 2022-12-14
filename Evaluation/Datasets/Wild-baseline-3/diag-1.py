def func(v10):
    # All elements with both indices equal need to be extracted, and are accumulated using the following list comprehension
    return [v10[v2][v2] for v2 in range(len(v10))]