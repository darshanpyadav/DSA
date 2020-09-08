'''
Given an array of integers A. There is a sliding window of size B which
is moving from the very left of the array to the very right.
You can only see the w numbers in the window. Each time the sliding window moves
rightwards by one position. You have to find the maximum for each window.
The following example will give you more clarity.

The array A is [1 3 -1 -3 5 3 6 7], and B is 3.

Window position	Max
———————————-	————————-
[1 3 -1] -3 5 3 6 7	3
1 [3 -1 -3] 5 3 6 7	3
1 3 [-1 -3 5] 3 6 7	5
1 3 -1 [-3 5 3] 6 7	5
1 3 -1 -3 [5 3 6] 7	6
1 3 -1 -3 5 [3 6 7]	7
Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

Note: If B > length of the array, return 1 element with the max of the array.



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1]
For Example

Input 1:
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
Output 1:
    C = [3, 3, 5, 5, 6, 7]
'''
from collections import deque


def slidingMaximum(A, B):
    # O(N*B)
    # if B > len(A):
    #     return max(A)
    #
    # max_arr = []
    #
    # for i in range(len(A)-B+1):
    #     max_arr.append(max(A[i:i+1+B]))
    #
    # return max_arr
    i = 0
    out = [max(A[i:i + B])]
    for i in range(len(A)-B):
        new = A[i+B]
        old = A[i]
        if new > out[-1]:
            out.append(new)
        else:
            if out[-1] == old:
                out.append(max(A[i+1:i+1+B]))
            else:
                out.append(out[-1])
    return out


A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3
print(slidingMaximum(A, B))
