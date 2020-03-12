# def spiral_matrix(A):
#     r = []
#     A = list(A)
#
#     while len(A):
#         # Right to left
#         r.extend(A[0])
#         A.pop(0)
#
#         # Top to bottom
#         for i in A[::]:
#             r.append(i[-1])
#             if len(i) == 1:
#                 A.pop(0)
#             else:
#                 i.pop()
#
#         if A:
#             # Left to right
#             r.extend(A[-1][::-1])
#             A.pop(-1)
#
#         # Bottom to top
#         l = len(A)
#         for index, i in enumerate(A[::-1]):
#             r.append(i[0])
#             if len(i) == 1:
#                 A.pop(l-1-index)
#             else:
#                 i.pop(0)
#     return r


def spiral_matrix(arr):
    r = []
    row_start = 0
    col_start = 0
    row_end = len(A)-1
    col_end = len(A[0])-1

    while row_start <= row_end and col_start <= col_end:
        # left to right
        for i in range(col_start, col_end+1):
            r.append(A[row_start][i])
        row_start += 1

        # top to bottom
        for i in range(row_start, row_end+1):
            r.append(A[i][col_end])
        col_end -= 1

        # right to left
        for i in range(col_end, col_start-1, -1):
            r.append(A[row_end][i])
        row_end -= 1

        # bottom to top
        for i in range(row_end, row_start-1, -1):
            r.append(A[col_start][i])
        col_start += 1

    return r




# A = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# A = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# A = [
#     [1]
# ]
# A = [
#     [1],
#     [2],
#     [3]
# ]
# A = [
#     [252, 60, 110, 389],
#     [311, 84, 264, 305],
#     [203, 118, 376, 90],
#     [37, 55, 223, 153],
#     [234, 335, 52, 263],
#     [207, 350, 272, 233],
#     [140, 327, 125, 168]
# ]
A = [
    [44],
    [36],
    [395],
    [179],
    [249],
    [349],
    [5],
    [139]
]
A = [
    [324, 168, 142, 201, 119],
    [245, 165, 307, 308, 115],
    [395, 249, 66, 37, 80],
    [28, 36, 374, 58, 370],
    [57, 350, 389, 124, 139],
    [91, 138, 185, 295, 343],
    [385, 248, 72, 202, 267],
    [308, 245, 282, 359, 16],
]


print(spiral_matrix(A))
