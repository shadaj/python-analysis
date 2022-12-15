import shape, transpose

def moveaxis_1(a, source, destination):

    shape_inp = shape.shape_1(a)
    dim_inp = len(shape_inp)

    if source < 0:
        source += dim_inp
    if destination < 0:
        destination += dim_inp

    transpose_axis = [i for i in range(dim_inp)]
    
    transpose_axis_1 = []
    for j, ax in enumerate(transpose_axis):
        if j == source:
            topick = ax
        else:
            transpose_axis_1.append(ax)
    transpose_axis = []
    for j, ax in enumerate(transpose_axis_1):
        if j == destination:
            transpose_axis.append(topick)
        transpose_axis.append(ax)
    if destination == len(transpose_axis_1):
        transpose_axis.append(topick)


    return transpose.transpose_1(a, transpose_axis)

def test_moveaxis():
    import numpy as np

    A = np.random.randint(0, 10, size=(1,))
    assert(np.moveaxis(A, 0, -1).tolist() == moveaxis_1(A.tolist(), 0, -1))

    A = np.random.randint(0, 10, size=(4,3))
    assert(np.moveaxis(A, 0, -1).tolist() == moveaxis_1(A.tolist(), 0, -1))

    A = np.random.randint(0, 10, size=(3,5,7,9,13))
    assert(np.moveaxis(A, 1, -1).tolist() == moveaxis_1(A.tolist(), 1, -1))

    A = np.random.randint(0, 10, size=(3,5,7,9,13))
    assert(np.moveaxis(A, -1, 1).tolist() == moveaxis_1(A.tolist(), -1, 1))
    