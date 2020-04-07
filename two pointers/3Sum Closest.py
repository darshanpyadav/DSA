'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)
'''


def threeSumClosest(A, B):
    # Can use either Front-back or Fast-slow pointers
    # We need 3 items hence at-least O(N^2) is needed
    prev_diff = float('inf')
    r = 0
    A = sorted(A)

    for i in range(len(A)):
        start, end = i+1, len(A)-1
        while start < end:
            a, b, c = A[i], A[start], A[end]
            s = a + b + c
            if s == B:
                return B
            if abs(s - B) < prev_diff:
                r = s
                prev_diff = abs(s-B)
            elif s > B:
                end -= 1
            else:
                start += 1

    return r


A = [1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3]
B = 2
A = [-1, 2, 1, -4]
B = 1
print(threeSumClosest(A, B))
