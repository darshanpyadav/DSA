'''
Given a matrix of integers A of size N x M and an integer B.

Write an efficient algorithm that searches for integar B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Input Format

The first argument given is the integer matrix A.
The second argument given is the integer B.
Output Format

Return 1 if B is present in A, else return 0.
Constraints

1 <= N, M <= 1000
1 <= A[i][j], B <= 10^6
For Example

Input 1:
    A =
    [ [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  ]
    B = 3
Output 1:
    1

Input 2:
    A = [   [5, 17, 100, 111]
            [119, 120,  127,   131]    ]
    B = 3
Output 2:
    0
'''


def searchMatrix(A, B):
    # O(logN)
    m = len(A)
    n = len(A[0])
    start, end = 0, m*n - 1

    while start <= end:
        mid = (start + end)//2
        start_i, end_i = mid // n, mid % n
        if A[start_i][end_i] == B:
            return 1
        elif A[start_i][end_i] > B:
            end = mid - 1
        else:
            start = mid + 1
    return 0


A = [ [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]  ]
print(searchMatrix(A, 3))
