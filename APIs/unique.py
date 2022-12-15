import sort

def unique_1(a):
    a = sort.sort_1(a, None)
    output = []
    last_elem = None

    for i, el in enumerate(a):
        if el != last_elem:
            last_elem = el
            output.append(el)

    return output

def test_unique():
    import numpy as np

    a = np.random.randint(0, 10, size=(1,))
    assert(np.unique(a).tolist() == unique_1(a.tolist()))

    a = np.random.randint(0, 10, size=(3,4,5))
    assert(np.unique(a).tolist() == unique_1(a.tolist()))