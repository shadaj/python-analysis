# def trial(a):
#     i = 0
#     while i < len(a):
#         a[i] = 10
#         i+=1
#     a[1] = a[2]
#     a[3] = a[0] + a[4]
#     t = a[5]
#     a[5], a[6] = a[6], a[5]
#     a[4], a[5] = t, a[4]

# def trial(a):
#     a[1] = a[2]
#     a[3] = a[0] + a[4]
#     t = a[5]
#     a[5], a[6] = a[6], a[5]
#     a[4], a[5] = t, a[4]

# def trial(a):
#     return [i for i in a]

# def trial(a):
#     if a:
#         print("Blah")
#     else:
#         print("Not blah")

# def trial(a):
#     a[0], a[1] = a[1], a[0] + a[2]
#     if a[1] > a[0]:
#         a[2] = a[1]

# def func(b, *a):
#     print(a, b)

# def trial(a):
#     func(*a)

def func(a, b, c=10, d=20, e=30):
    print(a, b, c, d)

def trial(a):
    func(a[0], a[1], d = a[2], c=a[1])