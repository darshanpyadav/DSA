'''
Find if Given number is power of 2 or not.
More specifically, find if given number can be expressed as 2^k where k >= 1.

Input:

number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
Output:

return 1 if the number is a power of 2 else return 0

Example:

Input : 128
Output : 1
'''


def intToBase2(num):
    return str(bin(num)[2:])


def power(A):
    if A == "1":
        return 0
    binary = intToBase2(int(A))
    if binary[0] == "1" and "1" not in binary[1:]:
        return 1
    return 0

    # n = int(A)
    # if n==1 :
    #     return 0
    # if n &(n-1)==0:
    #     return 1
    # else:
    #     return 0


print(power("1"))
