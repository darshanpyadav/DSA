'''
Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

 Example: Input :
    A : [1 3 5]
    k : 4
 Output : YES as 5 - 1 = 4
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Try doing this in less than linear space complexity.
'''


def diffPossible(A, B):
    # O(N^2)
    # for i in range(len(A)-1):
    #     start, end = i, len(A)-1
    #     while start < end:
    #         if A[end] == A[start] + B:
    #             return 1
    #         elif A[end] > A[start] + B:
    #             end -= 1
    #         else:
    #             start += 1
    #             end = len(A)-1
    # return 0

    # O(N)
    if len(A) == 1:
        return 0
    i, j = 0, 1
    while i < len(A) and j < len(A):
        print(A[i],  A[j])
        if A[j]-A[i] == B:
            return 1
        elif A[j] - A[i] < B:
            j += 1
        else:
            i = i+1
            j = i+1
    return 0


A = [1, 2, 3, 9, 13, 15]
B = 6
A = [1, 2, 2, 3, 4]
B = 0
A = [1, 2, 3]
B = 0
# A = [0, 1, 9, 10, 13, 17, 17, 17, 23, 25, 29, 30, 37, 38, 39, 39, 40, 41, 42, 60, 64, 70, 70, 70, 72, 75, 85, 85, 90,
#       91, 91, 93, 95]
# B = 83
print(diffPossible(A, B))
