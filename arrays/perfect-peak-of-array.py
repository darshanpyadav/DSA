'''
Problem Description

Given an integer array A of size N.

You need to check that whether there exist a element which is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it.

If it exists return 1 else return 0.

NOTE:

Do not consider the corner elements i.e A[0] and A[N-1] as the answer.


Problem Constraints
3 <= N <= 105

1 <= A[i] <= 109



Input Format
First and only argument is an integer array A containing N integers.



Output Format
Return 1 if there exist a element that is strictly greater than all the elements on left of it and strictly smaller than all the elements on right of it else return 0.



Example Input
Input 1:

 A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
Input 2:

 A = [5, 1, 4, 4]


Example Output
Output 1:

 1
Output 2:

 0
'''


def perfectPeak(A):
    n = len(A)

    if n <= 2:
        return 0

    min_arr = [0]*(n-1) + [A[-1]]
    max_arr = [A[0]] + [0]*(n-1)

    for i in range(1, n):
        max_arr[i] = max(A[i], max_arr[i-1])

    for i in range(n-2, -1, -1):
        min_arr[i] = min(min_arr[i+1], A[i])
        
    for i in range(1, n-1):
        if max_arr[i-1] < A[i] < min_arr[i+1]:
            return 1

    return 0
    

# print(perfectPeak([5, 1, 4, 3, 6, 8, 10, 7, 9]))
# print(perfectPeak([5, 1, 4, 4]))
print(perfectPeak([3, 5, 7]))
print(perfectPeak([3, 1, 7]))