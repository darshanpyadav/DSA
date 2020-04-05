'''
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.

Example:

Input :
Array = {1 1 0 1 1 0 0 1 1 1 }
M = 1

Output :
[0, 1, 2, 3, 4]

If there are multiple possible solutions, return the sequence which has the minimum start index.
'''


def maxone(A, B):
    # O(N^2)
    # if B > len(A):
    #     return list(range(len(A)))
    #
    # max_count = 0
    # x, y = -1, -1
    # for i in range(len(A)):
    #     m, count = B, 0
    #     for j in range(i, len(A)):
    #         if A[j] == 0:
    #             if m <= 0:
    #                 break
    #             m -= 1
    #         count += 1
    #     else:
    #         j += 1
    #     if count > max_count:
    #         x, y = i, j
    #         max_count = count
    # return list(range(x, y))


A = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
B = 1
A = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
B = 2
A = [0, 0, 0, 1]
B = 4
A = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
B = 1
A = [ 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0]
B = 4
print(maxone(A, B))
