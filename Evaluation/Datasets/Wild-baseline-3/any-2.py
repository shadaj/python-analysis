def func(v0):
    v3 = False
    for v2 in v0:
        # Typecasting all elements of input to boolean else the operation becomes equivalent to bitwise or
        v3 = v3 | bool(v2)
    return v3