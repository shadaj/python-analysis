## ARANGE

def arange_1(start, stop, step):
    while start < stop:
        yield start
        start += step

def arange_2(start,stop,step):
    i=start
    while i<stop:
        yield i
        i+=step

def arange_3(start,stop,step):
    l=[]
    while start<stop:
        l.append(start)
        start+=step
    return l

def arange_4(start, end, step):
    lst = []
    for i in range(start, end, step):
        lst.append(i)
    return lst

## ZEROS

def zeros_1(shape):
    if isinstance(shape, int):
        return [0] * shape
    elif len(shape) == 0:
        return 0
    else:
        return [zeros_1(shape[1:]) for i in range(shape[0])]

## ONES

def ones_1(shape):
    if isinstance(shape, int):
        return [1] * shape
    elif len(shape) == 0:
        return 1
    else:
        return [ones_1(shape[1:]) for i in range(shape[0])]

## EMPTY -> CLOSE TO ZEROS (HOW CAN I NOT INITIALIZE PYTHON VAR?)

def empty_1(shape):
    if isinstance(shape, int):
        return [0] * shape
    elif len(shape) == 0:
        return 0
    else:
        return [empty_1(shape[1:]) for i in range(shape[0])]


## SQRT 

def sqrt_1(n):
    if n == 0:
        return 0
    else:
        return sqrt_helper(n, 1)

def sqrt_helper(n, guess):
    if good_enough(n, guess):
        return guess
    else:
        return sqrt_helper(n, improve_guess(n, guess))

def good_enough(n, guess):
    return abs(guess * guess - n) < 0.00000001

def improve_guess(n, guess):
    return (guess + n / guess) / 2.0

def sqrt_2(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
      guess = (guess + x / guess) / 2.0
      i += 1
    return guess

def sqrt_3(n):
    return n**0.5

## LINSPACE



