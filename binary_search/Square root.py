'''
Given an integar A.

Compute and return the square root of A.

If A is not a perfect square, return floor(sqrt(A)).

DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY

Input Format

The first and only argument given is the integer A.
Output Format

Return floor(sqrt(A))
Constraints

1 <= A <= 10^9
For Example

Input 1:
    A = 11
Output 1:
    3

Input 2:
    A = 9
Output 2:
    3
'''
import math


def sqrt(A):
    if A == 1:
        return 1

    # Sqrt of A will be within A//2
    start, end = 1, A//2

    while start <= end:
        mid = (start+end)//2
        mid_squared = mid*mid
        if mid_squared == A:
            return mid
        elif mid_squared < A:
            start = mid + 1
        else:
            end = mid - 1
    return start-1


print(sqrt(1256))
print(sqrt(11))
print(sqrt(9))
print(sqrt(1))
