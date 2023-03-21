''':cvarProblem Description

You are given a 1D integer array B containing A integers.

Count the number of ways to split all the elements of the array into 3 contiguous parts so that the sum of elements in each part is the same.

Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])



Problem Constraints
1 <= A <= 105

-109 <= B[i] <= 109



Input Format
First argument is an integer A.

Second argument is an 1D integer array B of size A.



Output Format
Return a single integer denoting the number of ways to split the array B into three parts with the same sum.



Example Input
Input 1:

 A = 5
 B = [1, 2, 3, 0, 3]
Input 2:

 A = 4
 B = [0, 1, -1, 0]

Example Output
Output 1:

 2
Output 2:

 1


Example Explanation
Explanation 1:

 There are no 2 ways to make partitions -
 1. (1,2)+(3)+(0,3).
 2. (1,2)+(3,0)+(3).
Explanation 2:

 There is only 1 way to make partition -
 1. (0)+(-1,1)+(0).
 '''


# @param A : integer
# @param B : list of integers
# @return an integer
def solve(n, arr):
    arr_sum = sum(arr)
    if (arr_sum % 3) != 0:
        return 0

    partition_sum = arr_sum // 3
    count = cur_sum = first_partition_count = 0

    for i in range(n-1):
        cur_sum += arr[i]

        # First increment count if 2 * partition_sum occurs
        # count is incremented by first_partition_count times because,
        # for every increase of first_partition_count, count increases by first_partition_count times
        if cur_sum == (2 * partition_sum):
            count += first_partition_count

        if cur_sum == partition_sum:
            first_partition_count += 1

    return count


# print(solve(5, [1, 2, 3, 0, 3]))
# print(solve(4, [0, 1, -1, 0]))
# print(solve(10, [2, 5, -2, 2, -3, -2, 3, 5, -5, -2]))
# print(solve(5,[ 3, 3, -3, 3, 3 ]))
print(solve(9, [6, 4, 8, 2, -10, 3, 7, 9, 1]))
# (6,4), (8,2,-10,3,7), (9,1)
# (6,4,8,2,-10), (3,7), (9,1)
# (6,4), (8,2), (-10,3,7,9,1)
print(solve(11, [6, 4, 8, 2, -10, 2, -2, 3, 7, 9, 1]))
