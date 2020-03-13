'''
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
'''


# def firstMissingPositive(A):
#     # Time: O(N)
#     # Space: O(N)
#
#     d = {}
#     for i in A:
#         if i > 0:
#             d[i] = i
#
#     for i in range(1, len(d)+1):
#         try:
#             a = d[i]
#         except KeyError:
#             return i
#     return len(d) + 1


def firstMissingPositive(A):
    # Time: O(N)
    # Space: O(1)

    # Arrange element i at it's index
    for i in A[:]:
        if 0 < i <= len(A):
            A[i-1] = i

    # Check if element is at it's index starting from 1
    for i in range(1, len(A)+1):
        if i != A[i-1]:
            return i
    return len(A)+1


print(firstMissingPositive([2,3,7,6,8]))
print(firstMissingPositive([3,4,-1,1,7]))
print(firstMissingPositive([1,1,0]))
print(firstMissingPositive([-8,-7,-6]))
print(firstMissingPositive([2,3,6,8,1,15]))
