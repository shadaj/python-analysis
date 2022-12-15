import zeros_like, shape
import itertools

def search(a, v):
    st = 0
    en = len(a) - 1

    while st < en:
        
        mid = st + (en - st) // 2
        if v < a[mid]:
            en = mid - 1
        elif v > a[mid]:
            st = mid + 1
        else:
            en = mid - 1
    if a[st] < v:
        return st + 1
    return st

def searchsorted_1(a, v):
    output = zeros_like.zeros_like_1(v)
    shape_output = shape.shape_1(output)

    for indices in itertools.product(*[list(range(j)) for j in shape_output]):
        x = v
        for index in indices:
            x = x[index]
        
        out = output
        for i, index in enumerate(indices):
            if i + 1 == len(indices):
                out[index] = search(a, x)
            else:
                out = out[index]

    if len(shape_output) == 0:
        return search(a, v)
    else:
        return output

def test_searchsorted():
    import numpy as np

    for i in range(30):
        A = np.random.randint(0, 10, size=(16,))
        A = np.sort(A)
        print(A)
        assert(np.searchsorted(A, 0).tolist() == searchsorted_1(A.tolist(), 0))
        assert(np.searchsorted(A, 10).tolist() == searchsorted_1(A.tolist(), 10))
        assert(np.searchsorted(A, [[0, 1], [9, 10], [-1, 5]]).tolist() == searchsorted_1(A.tolist(), [[0, 1], [9, 10], [-1, 5]]))

        A = np.random.randint(0, 10, size=(5,))
        A = np.sort(A)
        print(A)
        assert(np.searchsorted(A, 0).tolist() == searchsorted_1(A.tolist(), 0))
        assert(np.searchsorted(A, 10).tolist() == searchsorted_1(A.tolist(), 10))
        assert(np.searchsorted(A, [[0, 1], [9, 10], [-1, 5]]).tolist() == searchsorted_1(A.tolist(), [[0, 1], [9, 10], [-1, 5]]))


        A = np.random.randint(0, 10, size=(15,))
        A = np.sort(A)
        print(A)
        assert(np.searchsorted(A, 0).tolist() == searchsorted_1(A.tolist(), 0))
        assert(np.searchsorted(A, 10).tolist() == searchsorted_1(A.tolist(), 10))
        assert(np.searchsorted(A, [[0, 1], [9, 10], [-1, 5]]).tolist() == searchsorted_1(A.tolist(), [[0, 1], [9, 10], [-1, 5]]))


