'''
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

 Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
'''


def removeDuplicates(A):
    # Fast/ slow
    slow = 0
    for fast in range(1, len(A)):
        if A[slow] != A[fast]:
            slow += 1
            A[slow] = A[fast]

    # return slow+1
    return A[:slow+1]


A = [0, 1, 1, 2, 3, 3, 3]
# A = [0]
print(removeDuplicates(A))
