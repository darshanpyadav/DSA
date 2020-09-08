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
 '''


# @param A : integer
# @param B : list of integers
# @return an integer
def solve(n, arr):
    arr_sum = sum(arr)
    if (arr_sum % 3) != 0:
        return 0

    equal_sum = arr_sum // 3
    count = cur_sum = i = 0

    for k in range(n):
        # First point is always fixed
        cur_sum += arr[k]

        if cur_sum == equal_sum:
            i += 1

        if cur_sum == (2 * equal_sum):
            count += i

    if equal_sum == 0:
        count = (i-1)*(i-2)//2

    return count


# print(solve(5, [1, 2, 3, 0, 3]))
# print(solve(4, [0, 1, -1, 0]))
# print(10, [ 2, 5, -2, 2, -3, -2, 3, 5, -5, -2 ])
print(solve(5,[ 3, 3, -3, 3, 3 ]))
