# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 19/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


def fib(n):
    m = {0: 1, 1: 1}
    for i in range(2, n+1):
        m[i] = m[i-1] + m[i-2]
    return m[n]


print(fib(10))

# O(N)