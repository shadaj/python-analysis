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

def trial(a):
    return [i for i in a]