'''
You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:

You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

Return answer modulo 109 + 7.

For example,

A = [1, 1, 1, 2, 2]

Return: 4

'''
from itertools import combinations


def nTriang(A):
    # count = 0
    # A = sorted(A)
    # for a, b, c in combinations(A, 3):
    #     if a <= 0 or b <= 0 or c <= 0:
    #         continue
    #     else:
    #         if a + b > c:
    #             count += 1
    # return count

    # Can use either Front-back or Fast-slow pointers
    # We need 3 items hence at-least O(N^2) is needed
    count = 0
    A.sort(reverse=True)
    for i in range(len(A)-2):
        start, end = i+1, len(A)-1
        while start < end:
            if A[start] + A[end] > A[i]:
                count += end - start
                start += 1
            else:
                end -= 1
    return count % 1000000007


A = [1, 1, 1, 2, 2]
A = [1, 1, 1, 1, 1]
A = [4, 6, 13, 16, 20, 3, 1, 12]
print(nTriang(A))
