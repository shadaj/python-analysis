def func(v0):
    # If the result is not a collection, we wrap it with a list
    if isinstance(v0, list):
        return v0
    else:
        return [v0]