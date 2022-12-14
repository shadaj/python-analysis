def func(v5):
    v89 = []
    for v0 in v5:
        # Filtering elements by what is already seen
        if v0 not in v89:
            v89.append(v0)
    return v89