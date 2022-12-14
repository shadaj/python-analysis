def func(v5,v41,v42):
    # This function appends the new value in the middle of an array
    v5.append(0)
    for v2 in range(len(v5)-1,v41,-1):
        v5[v2]=v5[v2-1]
    v5[v41]=v42
    return v5