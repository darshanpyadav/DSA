'''
Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input :
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]
 NOTE : For the purpose of this problem ( as also conveyed by the sample case ), assume that elements that appear more than once in both arrays should be included multiple times in the final output.
'''


def intersect(A, B):
    i, j = 0, 0
    res = []

    if B[0] > A[-1] or B[-1] < A[0]:
        return res

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            res.append(A[i])
            i, j = i+1, j+1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return res


a = [1, 2, 3, 3, 4, 5, 6]
b = [3, 3, 5]

print(intersect(a, b))
