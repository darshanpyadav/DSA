'''
    N = {3, 5, 10}
    Input: n = 20 -> output: 4
    There are the following 4 ways to reach 20:
    (10, 10)
    (5, 5, 10)
    (5, 5, 5, 5)
    (3, 3, 3, 3, 3, 5)
'''

N = 20
S = [3, 5, 10]   #Order doesn't matter

# *******************************Recursive solution********************************


def count(n, s, i):
    if n == 0:
        return 1
    elif n < 0 or i < 0:
        return 0
    elif s[i] > n:
        return count(n, s, i-1)
    else:
        return count(n - s[i], s, i) + count(n, s, i-1)


print(count(N, S, len(S)-1))

# ******************************* DP solution **************************************
m = {}


def count_dp(n, s, i):
    key = str(i) + "_" + str(n)
    if key in m:
        return m[key]
    if n == 0:
        return 1
    elif n < 0 or i < 0:
        return 0
    elif s[i] > n:
        val = count_dp(n, s, i-1)
    else:
        val = count_dp(n - s[i], s, i) + count_dp(n, s, i-1)
    m[key] = val
    return val


print(count_dp(N, S, len(S)-1))
