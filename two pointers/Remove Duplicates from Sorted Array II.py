'''
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].
'''


def removeDuplicates(A):
    slow = 0
    count = 1
    for fast in range(1, len(A)):
        if (count < 2 and A[fast] == A[slow]) or (A[fast] != A[slow]):
            count = count + 1 if A[fast] == A[slow] else 1
            slow += 1
            A[slow] = A[fast]

    return A[:slow+1]

# A = [0,1,1,2,3,3,3]
A = [1, 1, 1, 2, 2, 3, 3, 3, 3]
print(removeDuplicates(A))