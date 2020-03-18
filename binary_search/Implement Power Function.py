'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
'''


def pow_fun(x, n, d):
    x = x - (d * (x / d))
    if n == 1:
        return x
    if n == 0:
        return 1 if x != 0 else 0
    extra = x if n - (2 * (n // 2)) == 1 else 1
    sol = extra * pow_fun(x * x, n // 2, d)
    return sol - (d * (sol / d))


print(pow_fun(2, 3, 3))
# print(pow(3,8,8))
# print(pow(0, 121, 8))
# print(pow(-5, 21, 6))
