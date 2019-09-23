# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 21/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************
import numpy as np


def lcs(u, v):
    """Return c where c[i][j] contains length of LCS of u[i:] and v[j:]."""
    c = [[-1]*(len(v)+1) for _ in range(len(u) + 1)]

    for i in range(len(u)+1):
        c[i][len(v)] = 0
    for j in range(len(v)+1):
        c[len(u)][j] = 0

    for i in range(len(u)-1, -1, -1):
        for j in range(len(v)-1, -1, -1):
            if u[i] == v[j]:
                c[i][j] = 1 + c[i+1][j+1]
            else:
                c[i][j] = max(c[i][j+1], c[i+1][j])

    return c


def print_lcs(u, v, c):
    """Print one LCS of u and v using table c."""
    i = j = 0
    while not (i == len(u) or j == len(v)):
        if u[i] == v[j]:
            print(u[i], end="")
            i += 1
            j += 1
        else:
            if c[i][j+1] > c[i+1][j]:
                j += 1
            else:
                i += 1


if __name__ == "__main__":
    u = input('Enter first string: ')
    v = input('Enter second string: ')
    c = lcs(u, v)
    print('Longest Common Subsequence: ', end='')
    print_lcs(u, v, c)
    print()
    print(np.matrix(c))


# O(M*N)