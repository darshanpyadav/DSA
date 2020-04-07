'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

 Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets. For example, given array S = {-1 0 1 2 -1 -4},
A solution set is:
(-1, 0, 1)
(-1, -1, 2)
'''


def threeSum(A):
    # Can use either Front-back or Fast-slow pointers
    # We need 3 items hence at-least O(N^2) is needed
    A = sorted(A)
    s = set()
    # for i in range(len(A)-2):
    #     start, end = i+1, i+2
    #     while start < len(A)-1 and end < len(A):
    #         print(i, start, end)
    #         a, b, c = A[i], A[start], A[end]
    #         if a + b + c == 0:
    #             s.add((a, b, c))
    #             start = start + 1
    #             end = start + 1
    #         elif a + b + c < 0:
    #             end += 1
    #         else:
    #             start += 1
    # return list(map(list, sorted(s)))

    for i in range(len(A)-2):
        start, end = i+1, len(A)-1
        while start < end:
            a, b, c = A[i], A[start], A[end]
            if a + b + c == 0:
                s.add((a, b, c))
                start, end = start + 1, end - 1
            elif a + b + c < 0:
                start += 1
            else:
                end -= 1
    return list(map(list, sorted(s)))


A = [-1, 0, 1, 2, -1, -4]
# A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
print(threeSum(A))