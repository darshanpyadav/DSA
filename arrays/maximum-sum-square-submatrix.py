'''
Problem Description

Given a 2D integer matrix A of size N x N find a B x B submatrix where B<= N and B>= 1, such that sum of all the elements in submatrix is maximum.



Problem Constraints
1 <= N <= 103.

1 <= B <= N

-102 <= A[i][j] <= 102.



Input Format
First arguement is an 2D integer matrix A.

Second argument is an integer B.



Output Format
Return a single integer denoting the maximum sum of submatrix of size B x B.



Example Input
Input 1:

 A = [
        [1, 1, 1, 1, 1]
        [2, 2, 2, 2, 2]
        [3, 8, 6, 7, 3]
        [4, 4, 4, 4, 4]
        [5, 5, 5, 5, 5]
     ]
 B = 3
Input 2:

 A = [
        [2, 2]
        [2, 2]
    ]
 B = 2


Example Output
Output 1:

 48
Output 2:

 8


Example Explanation
Explanation 1:

    Maximum sum 3 x 3 matrix is
    8 6 7
    4 4 4
    5 5 5
    Sum = 48
Explanation 2:

 Maximum sum 2 x 2 matrix is
  2 2
  2 2
  Sum = 8
'''


def solve(A, B):
    # n = len(A)
    #
    # if n == 1:
    #     return A[0]
    # row_prefix_sum = [[0] * (n + 1 - B) for _ in range(n)]
    #
    # for i in range(n):
    #     for j in range(n + 1 - B):
    #         row_prefix_sum[i][j] = sum(A[i][j:j+B])
    #
    # max_sum = 0
    # for i in range(n + 1 - B):
    #     for j in range(n + 1 - B):
    #         cur_sum = 0
    #         for k in range(B):
    #             cur_sum += row_prefix_sum[j+k][i]
    #             if cur_sum > max_sum:
    #                 max_sum = cur_sum
    #
    # return max_sum
    n = len(A)
    col_prefix_sum = [[0]*n for _ in range(n + 1 - B)]
    max_sum = -float('inf')

    for i in range(n):
        cur_sum = 0
        # For the first row in the col_prefix_sum
        for j in range(B):
            cur_sum += A[j][i]
        col_prefix_sum[0][i] = cur_sum

        for k in range(1, n + 1 - B):
            cur_sum += A[B + k-1][i] - A[k-1][i]
            col_prefix_sum[k][i] = cur_sum

    for i in range(n + 1 - B):
        for j in range(n + 1 - B):
            cur_sum = sum(col_prefix_sum[i][j: j+B])
            if cur_sum > max_sum:
                max_sum = cur_sum
    return max_sum


A = [
    [1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2],
    [3, 8, 6, 7, 3, 3],
    [4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 5]
]
B = 3

A = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 8, 6, 7],
    [4, 4, 4, 4],
]
B = 2
# A = [
#     [2, 2],
#     [2, 2]
# ]
# B = 2
#
# A = [
#     [-33, 34, 0, 69, 24, -22, 58, 62, -36, 5, 45, -19, -73, 61, -9, 95],
#     [42, -73, -64, 91, -96, 2, 53, -8, 82, -79, 16, 18, -5, -53, 26, 71],
#     [38, -31, 12, -33, -1, -65, -6, 3, -89, 22, 33, -27, -36, 41, 11, -47],
#     [-32, 47, -56, -38, 57, -63, -41, 23, 41, 29, 78, 16, -65, 90, -58, -12],
#     [6, -60, 42, -36, -52, -54, -95, -10, 29, 70, 50, -94, 1, 93, 48, -71],
#     [-77, -16, 54, 56, -60, 66, 76, 31, 8, 44, -61, -74, 23, 37, 38, 18],
#     [-18, 29, 41, -67, 15, -61, -42, 4, 30, 77, 6, -27, 86, -79, 45, 24],
#     [-28, -30, -71, 77, 73, -3, 12, 86, -10, 61, -64, 55, 67, -45, 74, -69],
#     [-48, 50, 50, 41, 24, 66, -70, 7, 91, -93, 37, -43, -13, 53, 83, 45],
#     [9, -91, 58, -79, 88, -78, 46, 6, -70, -87, 68, 0, 91, 62, -45, -90],
#     [59, -76, 37, 48, -17, 95, -59, -98, 50, -9, -64, 74, -80, 96, -79, 48],
#     [99, -32, -16, -19, 34, -47, 99, -82, 38, 0, 88, 27, -33, 28, -7, -52],
#     [-17, -93, -79, 10, -83, -87, 14, 9, -84, 35, -49, -100, -51, 19, 56, 98],
#     [3, -76, -92, -56, -91, 89, 2, 95, -15, -7, 43, 23, 87, 14, 3, -52],
#     [-100, -42, -82, 80, 96, 98, -19, 89, 98, -91, 57, -28, -78, 38, -8, -62],
#     [79, 90, -43, 58, 91, -85, -12, 56, 11, -98, -66, -28, -45, 28, -54, 62]
# ]
# B = 7
print(solve(A, B))
