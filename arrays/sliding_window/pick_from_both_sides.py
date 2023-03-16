'''
Problem Description

Given an integer array A of size N.

You can pick B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then:

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.


Problem Constraints
1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you picked.



Example Input
Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [1, 2]
 B = 1


Example Output
Output 1:

 8
Output 2:

 2
'''


def solve(arr, k):
    # window type: static
    # window size: k

    # we are initializing the max_sum to be the sum of last k elements of the list
    max_sum = cur_sum = sum(arr[-k:])

    for index in range(k):
        # slide window to the front of the list
        # arr[-k] -> points to the k element from the back of the list
        cur_sum += - arr[-k + index] + arr[index]
        max_sum = max(max_sum, cur_sum)
    return max_sum


print(solve([5, -2, 3 , 1, 2], 3))
print(solve([ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436,
              -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894
                , -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741,
              529, -222, -684, 35 ], 48))
