def func(v0):
    for v2 in v0:
        # If any one element is true, the result cannot be false
        if v2:
            return True
    return False