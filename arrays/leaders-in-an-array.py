'''
Problem Description

Given an integer array A containing N distinct integers, you have to find all the leaders in the array A.

An element is leader if it is strictly greater than all the elements to its right side.

NOTE:The rightmost element is always a leader.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 108



Input Format
First and only argument is an integer array A.



Output Format
Return an integer array denoting all the leader elements of the array.

NOTE: Ordering in the output doesn't matter.



Example Input
Input 1:

 A = [16, 17, 4, 3, 5, 2]
Input 2:

 A = [1, 2]


Example Output
Output 1:

 [17, 2, 5]
Output 2:

 [2]
'''


def solve(A):
    # n = len(A)
    # max_prefix_arr = [float('-inf')]*(n-1)
    # max_prefix_arr.append(A[-1])
    # res = []
    #
    # for i in range(n-2, -1, -1):
    #     max_prefix_arr[i] = max(max_prefix_arr[i+1], A[i])
    #
    # for i in range(n-1):
    #     if A[i] > max_prefix_arr[i+1]:
    #         res.append(A[i])
    #
    # res.append(A[-1])
    # return res

    n = len(A)
    res = [A[-1]]

    for i in range(n-2, -1, -1):
        if A[i] > res[-1]:
            res.append(A[i])

    return res


print(solve([16, 17, 4, 3, 5, 2]))
print(solve([1, 2]))