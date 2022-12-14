def func(v31, v70):
    if len(v31) != v70[0]*v70[1]:
        return None
    else:
        # organizing the result using flattened indexes 
        return [v31[v2:v2+v70[1]] for v2 in range(0, len(v31), v70[1])]