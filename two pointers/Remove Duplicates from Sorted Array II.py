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
    # prev_index, prev_val = 0, A[0]
    # count = 1
    # for i in range(1, len(A)):
    #     if A[i] == prev_val:
    #         if count < 2:
    #             count, prev_index = count+1, prev_index+1
    #             A[prev_index] = A[i]
    #     else:
    #         prev_index, prev_val = prev_index+1, A[i]
    #         A[prev_index] = A[i]
    #         count = 1
    #
    # return A[:prev_index+1]

    nums = A
    count = 0
    for i in range(len(nums)):
        if count < 2 or nums[count - 2] != nums[i]:
            nums[count] = nums[i]
            count += 1
    return nums[:count]


# A = [0,1,1,2,3,3,3]
A = [1, 1, 1, 2, 2, 3, 3, 3, 3]
print(removeDuplicates(A))