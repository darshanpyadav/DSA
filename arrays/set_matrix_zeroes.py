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