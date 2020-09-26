"""
 A = [5, 10, 3, 2, 50, 80]
 B = 78
"""


def solve(A, B):
    A.sort()
    slow, fast = 0, 0

    while slow < len(A) and fast < len(A):
        if A[fast] - A[slow] == B and slow != fast:
            return 1
        elif A[fast] - A[slow] < B:
            fast += 1
        else:
            slow += 1
    return 0

