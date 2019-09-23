# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 23/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


def lcw(u, v):
    """Return length of an LCW of strings u and v and its starting indexes.

    (l, i, j) is returned where l is the length of an LCW of the strings u, v
    where the LCW starts at index i in u and index j in v.
    """
    # c[i][j] will contain the length of the LCW at the start of u[i:] and
    # v[j:].
    c = [[0]*(len(v)+1) for _ in range(len(u)+1)]

    length_lcw = 0
    m, n = -1, -1
    for i in range(len(u)-1, -1, -1):
        for j in range(len(v)-1, -1, -1):
            if u[i] == v[j]:
                c[i][j] = 1 + c[i+1][j+1]
            if c[i][j] > length_lcw:
                length_lcw = c[i][j]
                m, n = i, j

    return length_lcw, m, n


if __name__ == "__main__":
    u = input('Enter first string: ')
    v = input('Enter second string: ')
    l, i = lcw(u, v)
    print('Longest Common Subsequence: ', end='')
    # print(np.matrix(c))
    print(u[i:i+l] if l > 0 else "")

# O(M*N)
