'''
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
'''


def firstMissingPositive(A):
    # Time: O(N)
    # Space: O(N)

    d = {}
    for i in A:
        if i > 0:
            d[i] = i

    for i in range(1, len(d)+1):
        try:
            a = d[i]
        except KeyError:
            return i
    return len(d) + 1
# *****************************************************************************


def firstMissingPositive(nums):
    # Time: O(N)
    # Space: O(1)

    # Arrange element i at it's index
    if not nums:
        return 1
    i = 0
    length = len(nums)
    while i < length:
        current = nums[i]
        if current <= 0 or current > length or nums[current - 1] == current:
            i += 1
        else:
            nums[current - 1], nums[i] = nums[i], nums[current - 1]

    # Check if element is at it's index starting from 1
    for i in range(1, len(nums)+1):
        if i != nums[i-1]:
            return i
    return len(nums)+1


# print(firstMissingPositive([2,3,7,6,8]))
# print(firstMissingPositive([3,4,-1,1,7]))
# print(firstMissingPositive([1,1,0]))
# print(firstMissingPositive([-8,-7,-6]))
print(firstMissingPositive([2,3,6,8,1,15]))
