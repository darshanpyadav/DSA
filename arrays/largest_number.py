from functools import cmp_to_key


def sort_fun(a, b):
    print(a, b)
    return int(b+a) - int(a+b)


def largestNumber(A):
    A = sorted(map(str, A), key=cmp_to_key(sort_fun))
    res = ''.join(A).lstrip('0')
    return res or '0'
    

print(largestNumber([34, 30, 3, 5, 9]))
# print(largestNumber([ 12, 121 ]))
