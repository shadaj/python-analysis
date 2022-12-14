def func(v71):
    for v2 in range(len(v71)):
        # Flipping elements if required
        for v8 in range(v2+1, len(v71)):
            if v71[v2] > v71[v8]:
                v71[v2], v71[v8] = v71[v8], v71[v2]
    return v71