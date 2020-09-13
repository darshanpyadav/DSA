'''
Problem Description

Given an integer array A of size N. You need to count the number of special elements in the given array.

A element is special if removal of that element make the array balanced.

Array will be balanced if sum of even index element equal to sum of odd index element.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A of size N.



Output Format
Return an integer denoting the count of special elements.



Example Input
Input 1:

 A = [2, 1, 6, 4]
Input 2:

 A = [5, 5, 2, 5, 8]


Example Output
Output 1:

 1
Output 2:

 2
'''


def solve(A):
    n = len(A)
    even_sum = odd_sum = 0
    for i in range(n):
        if i % 2 == 0:
            even_sum += A[i]
        else:
            odd_sum += A[i]

    count = 0
    prev_even_sum = prev_odd_sum = 0
    for i in range(n):
        if i % 2 == 0:
            even_sum -= A[i]
        else:
            odd_sum -= A[i]

        # When you remove an element, the previous odd element will become an even ele,
        # and an even el becomes an odd ele
        # So total even_sum = even_sum + prev_odd_sum
        # So total odd_sum = odd_sum _prev_even_sum
        if even_sum + prev_odd_sum == odd_sum + prev_even_sum:
            count += 1

        if i % 2 == 0:
            prev_even_sum += A[i]
        else:
            prev_odd_sum += A[i]
    return count


print(solve([5, 5, 2, 5, 8]))