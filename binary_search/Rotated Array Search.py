'''
Given an array of integers A of size N and an integer B.

array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

You are given a target value B to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

NOTE:- Array A was sorted in non-decreasing order before rotation.

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

Return index of B in array A, otherwise return -1
Constraints

1 <= N <= 1000000
1 <= A[i] <= 10^9
all elements in A are disitinct.
For Example

Input 1:
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    B = 4
Output 1:
    0
Explanation 1:
 Target 4 is found at index 0 in A.


Input 2:
    A = [5, 17, 100, 3]
    B = 6
Output 2:
    -1
'''


def search(A, B):
    n = len(A)
    start, end = 0, len(A)-1

    while start <= end:
        mid = (start+end)//2
        if A[mid-1] > A[mid] < A[mid+1]:
            start_index = mid
            break
        if A[start] < A[end] or A[mid] < A[start]:
            end = mid - 1
        else:
            start = mid + 1
    else:
        start_index = start

    start, end = 0, n-1
    
    while start <= end:
        mid = (start+end)//2
        new_mid = (mid + start_index) % n
        if A[new_mid] == B:
            return new_mid
        elif A[new_mid] > B:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(search([6,7,0,1,2,3,4,5], 8))
print(search([ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ], 202))