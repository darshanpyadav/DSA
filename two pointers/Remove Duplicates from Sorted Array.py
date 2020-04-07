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
    prev_index = 0
    for i in range(1, len(A)):
        if A[i] != A[prev_index]:
            prev_index += 1
            A[prev_index] = A[i]

    return A[:prev_index+1]


A = [0, 1, 1, 2, 3, 3, 3]
# A = [0]
print(removeDuplicates(A))
