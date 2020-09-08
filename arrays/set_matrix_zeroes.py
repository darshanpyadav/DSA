'''
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.

Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

Input Format:

The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.
Output Format:

Return a 2-d matrix that satisfies the given conditions.
Constraints:

1 <= N, M <= 1000
0 <= A[i][j] <= 1
Examples:

Input 1:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]

Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]

Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]

Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]
'''


def setZeroes(A):
    index_i = set()
    index_j = set()
    m = len(A)
    n = len(A[0])

    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                index_i.add(i)
                index_j.add(j)

    for i in index_i:
        A[i] = [0]*n

    for j in index_j:
        for y in range(m):
            A[y][j] = 0

    return A



A = [   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]

A = [   [1, 1, 1],
        [1, 1, 1],
        [1, 0, 1]   ]
A = [
    [0, 0],
    [1, 1]
]
print(setZeroes(A))