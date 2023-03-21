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

import math
from bisect import bisect_left


# This function is used to get the left  most "index" where the
# element is inserted in the sorted list
def search_small(l, ele):
    # bisect left is used to maintain order in sorted list
    # gives index where ele should be inserted to maintain sorted order
    index = bisect_left(l, ele)
    # We'll also update the sorted list by adding ele to current sorted list
    l.insert(index, ele)
    # index-1 will give the element smaller than the current "ele"
    return index-1


def solve(A):
    n = len(A)

    # calculate max sum suffix array
    max_sum_suffix_arr = [0]*n
    max_sum_suffix_arr[-1] = A[-1]

    for i in range(n-2, -1, -1):
        max_sum_suffix_arr[i] = max(A[i], max_sum_suffix_arr[i+1])

    # Now calculate the element that is smaller than the current number frm the list that has elements from prev indices
    max_sum = -math.inf
    sorted_prev_list = [A[0]]
    for cur_index in range(1, n-1):
        smallest_index = search_small(sorted_prev_list, A[cur_index])
        # smallest_index == -1 when there is no smallest element than A[cur_index] in sorted list
        if smallest_index != -1 and A[cur_index] < max_sum_suffix_arr[cur_index+1]:
            max_sum = max(max_sum, sorted_prev_list[smallest_index] + A[cur_index] + max_sum_suffix_arr[cur_index+1])

    return max_sum if max_sum > 0 else 0


for arr in [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]:
    print(solve(arr))