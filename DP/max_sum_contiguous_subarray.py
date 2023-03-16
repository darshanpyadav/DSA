'''
Find the contiguous subarray within an array, A of length N which has the largest sum.

Input Format:

The first and the only argument contains an integer array, A.
Output Format:

Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:

1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:

Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6

Explanation 2:
    The subarray [4,-1,2,1] has the maximum possible sum of 6.
'''
#  Kadane's algorithm

# max_sum = 0
# current_sum = 0

# for i in a
# current_sum += + a[i]
# if max_sum < current_sum
#       max_sum = current_sum
# if current_sum < 0
#       current_sum = 0

import math


def max_sum_kadane(l):
    """
    Kadane's algorithm to calculate max contiguous subarray

    Define two-variable currSum which stores maximum sum ending here and maxSum which stores maximum sum so far.
    Initialize currSum with 0 and maxSum with INT_MIN.
    Now, iterate over the array and add the value of the current element to currSum and check
        If currSum is greater than maxSum, update maxSum equals to currSum.
        If currSum is less than zero, make currSum equal to zero.
    Finally, print the value of maxSum.
    """
    current_sum, max_sum = 0, -math.inf

    for ele in l:
        current_sum += ele

        if current_sum > max_sum:
            max_sum = current_sum
        # max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
        # current_sum = max(0, current_sum)
    return max_sum


# *****************************************************************************
# Using DP


def max_sum_dp(l):
    current_sum, max_sum = 0, -math.inf

    for ele in l:
        # we can either extend the maximum sum subarray seen so far by including the current element ele
        # (or) start a new maximum sum subarray at the current element ele
        # so we'll choose the maximum of them
        current_sum = max(ele, current_sum + ele)
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    # _, *a = map(int, input("a=").split())
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_sum_kadane(a))
    print(max_sum_dp(a))
