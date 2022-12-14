def func(v0):
    for v2 in v0:
        # If any single value of the input is false, the result is guaranteed to be false
        if bool(v2) == False:
            return False
    return True