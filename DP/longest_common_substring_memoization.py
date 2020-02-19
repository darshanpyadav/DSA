# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 23/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************
import numpy as np
import timeit


def lcw(u, v):
    """Return length of an LCW of strings u and v and its starting indexes.

   (l, m, n) is returned where l is the length of an LCW of the strings u, v
   where the LCW starts at index m in u and index n in v.
   """
    c = [[-1]*(len(v)+1) for _ in range(len(u)+1)]
    length_lcw = 0
    m, n = -1, -1
    for i in range(len(u)):
        for j in range(len(v)):
            temp = lcw_helper(u, v, c, i, j)
            if temp > length_lcw:
                length_lcw = temp
                m, n = i, j
    return length_lcw, m, n


def lcw_helper(u, v, c, i, j):
    """Return length of the LCW starting at u[i:] and v[j:] and fill table c.

    c[i][j] contains the length of the LCW at the start of u[i:] and v[j:].
    This function fills in c as smaller subproblems for solving c[i][j] are
    solved."""
    if c[i][j] > 0:
        return c[i][j]
    if i == len(u) or j == len(v):
        q = 0
    else:
        if u[i] == v[j]:
            q = 1 + lcw_helper(u, v, c, i+1, j+1)
        else:
            q = 0
    c[i][j] = q
    return q


if __name__ == "__main__":
    # u = input('Enter first string: ')
    # v = input('Enter second string: ')
    # l, i = lcw(u, v)
    # print('Longest Common Subsequence: ', end='')
    # # print(np.matrix(c))
    # print(u[i:i+l] if l > 0 else "")
    print("**************MEMOIZATION*************")
    print(timeit.repeat("lcw('bisect','trisect')",
                        "from darshan.DP.longest_common_substring_memoization import lcw", number=10000))
    print("**************BOTTOM UP*************")
    print(timeit.repeat("lcw('bisect','trisect')",
                        "from darshan.DP.longest_common_substring_bottom_up import lcw", number=10000))

# O(M*N)
