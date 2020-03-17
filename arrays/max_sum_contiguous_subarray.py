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


def max_sum(l):
    current_sum = 0
    curr = 0
    max_sum = l[0]
    start, end = 0, 0

    for i, el in enumerate(l):
        current_sum += el
        if max_sum < current_sum:
            max_sum = current_sum
            start = curr
            end = i
        if current_sum < 0:
            current_sum = 0
            curr += 1
    return max_sum, start, end

# *****************************************************************************
# Using DP


def max_sum_dp(l):
    current_sum = l[0]
    max_sum = l[0]
    for i in l:
        current_sum = max(i, current_sum + i)
        max_sum = max(current_sum, max_sum)
    return max_sum


if __name__ == "__main__":
    # _, *a = map(int, input("a=").split())
    # a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    max_sum, s, e = max_sum(a)
    print(max_sum, s, e)
    print(max_sum_dp(a))
