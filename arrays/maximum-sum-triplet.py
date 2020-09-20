'''
Problem Description

Given an array A containing N integers.

You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and Ai < Aj < Ak.

If no such triplet exist return 0.



Problem Constraints
3 <= N <= 105.

1 <= A[i] <= 108.



Input Format
First argument is an integer array A.



Output Format
Return a single integer denoting the maximum sum of triplet as described in the question.



Example Input
Input 1:

 A = [2, 5, 3, 1, 4, 9]
Input 2:

 A = [1, 2, 3]


Example Output
Output 1:

 16
Output 2:

 6
'''

from bisect import bisect_left


def search_small(l, ele):
    index = bisect_left(l, ele)
    if index:
        return index-1
    else:
        return -1


def solve(A):
    n = len(A)

    # calculate max sum suffix array
    max_sum_suffix_arr = [0]*n
    max_sum_suffix_arr[-1] = A[-1]

    for i in range(n-2, -1, -1):
        max_sum_suffix_arr[i] = max(A[i], max_sum_suffix_arr[i+1])

    # Now calculate the element that is smaller than the current number frm the list that has elements from prev indices

    max_sum = float('-inf')
    sorted_prev_list = [A[0]]
    for i in range(1, n-1):
        res = search_small(sorted_prev_list, A[i])
        if res != -1 and A[i] < max_sum_suffix_arr[i+1]:
            max_sum = max(max_sum, sorted_prev_list[res] + A[i] + max_sum_suffix_arr[i+1])
        sorted_prev_list.insert(res+1, A[i])

    return max_sum
