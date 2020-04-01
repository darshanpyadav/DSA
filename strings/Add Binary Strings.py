'''
Given two binary strings, return their sum (also a binary string).

Example:

a = "100"

b = "11"
Return a + b = “111”.
'''


def base2ToInt(str_n):
    return int(str_n, 2)


def intToBase2(num):
    return str(bin(num)[2:])


def addBinary(A, B):
    return str(intToBase2((base2ToInt(A) + base2ToInt(B))))


a = "100"
b = "11"
print(addBinary(a, b))
