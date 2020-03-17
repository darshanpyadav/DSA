'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]
'''


from copy import deepcopy


def rotate(A):
    B = deepcopy(A)
    l = len(A)

    m, n = -1, -1
    for j in range(l):
        m, n = m+1, 0
        for i in range(l-1, -1, -1):
            A[m][n] = B[i][j]
            n += 1

    return A


A = [
    [1,2],
    [3,4]
]
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(rotate(A))
