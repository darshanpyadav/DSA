'''
Input:

1 2 3
4 5 6
7 8 9

Return the following :

[
    [1],
    [2, 4],
    [3, 5, 7],
    [6, 8],
    [9]
]
'''


# def anti_diagonals(A):
#     r = []
#     if len(A) == 1:
#         return [A[0][0]]
#     i, j, z = 0, 0, 0
#     while j < len(A) and z < len(A):
#         a = []
#         k = j
#         if j < len(A) - 1:
#             i = 0
#         else:
#             i = z
#             z += 1
#         while i <= j:
#             a.append(A[i][k])
#             i += 1
#             k -= 1
#         r.append(a)
#         if j < len(A) - 1:
#             j += 1
#     return r

# There are 2n - 1 diagonals, hence set them to []
# Sum of indexes anti diagonals will be same, hence append all the common ones. T
def anti_diagonals(A):
    d = {}
    n = len(A)
    for i in range(2*n - 1):
        d[i] = []

    for i in range(n):
        for j in range(n):
            l = i + j
            d[l].append(A[i][j])

    return list(d.values())


A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# A = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# A = [
#     [0]
# ]
print(anti_diagonals(A))
