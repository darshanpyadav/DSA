'''
Given a matrix of integers A of size N x M in which each row is sorted.

Find an return the overall median of the matrix A.

Note: No extra memory is allowed.

Note: Rows are numbered from top to bottom and columns are numbered from left to right.



Input Format

The first and only argument given is the integer matrix A.
Output Format

Return the overall median of the matrix A.
Constraints

1 <= N, M <= 10^5
1 <= N*M  <= 10^6
1 <= A[i] <= 10^9
N*M is odd
For Example

Input 1:
    A = [   [1, 3, 5],
            [2, 6, 9],
            [3, 6, 9]   ]
Output 1:
    5
Explanation 1:
    A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
    Median is 5. So, we return 5.

Input 2:
    A = [   [5, 17, 100]    ]
Output 2:
    17 ``` Matrix=
'''


def findMedian(A):
    # Time:  O(MNLog(MN))
    # Space: O(MN)
    if len(A) == 0:
        return []

    # O(MN)
    arr = []
    for i in range(len(A)):
        arr.extend(A[i])

    # O(M*N*Log(M*N) or use heapify to build heap and pop till middle element
    arr = sorted(arr)

    return arr[len(arr)//2]
# **********************************************************************************************************************


from bisect import bisect_right


def findMedian(A):
    if len(A) == 0:
        return []

    m, n = len(A), len(A[0])
    min_element, max_element = float('inf'), float('-inf')

    # Number of elements should be present on either sides
    k = (m*n + 1)//2

    for i in range(m):
        min_element = min(min_element, A[i][0])
        max_element = max(max_element, A[i][-1])

    # For median, number of elements on either sides are same == (mn)//2
    while min_element <= max_element:
        mid = (min_element + max_element)//2

        count = 0
        for row in A:
            # number of elements smaller than element
            count += bisect_right(row, mid)

        if count < k:
            min_element = mid + 1
        else:
            max_element = mid - 1

    return min_element


A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]   ]
A = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
print(findMedian(A))