'''
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 400 500]
B : [2 3]

Sample Output

3
 NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element.
For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
'''
from bisect import bisect_right


def get_min_val(min_val, max_val, A, B, k):
    while min_val <= max_val:
        mid = (min_val+max_val)//2
        count = bisect_right(A, mid) + bisect_right(B, mid)
        if count < k+1:
            min_val = mid + 1
        else:
            max_val = mid - 1
    return min_val


def findMedianSortedArrays(A, B):
    if not len(A):
        min_val, max_val = B[0], B[-1]

    if not len(B):
        min_val, max_val = A[0],  A[-1]

    if len(A) and len(B) > 0:
        min_val, max_val = min(A[0], B[0]), max(A[-1], B[-1])

    l = len(A) + len(B)

    if l % 2 != 0:
        return get_min_val(min_val, max_val, A, B, l//2)
    else:
        return (get_min_val(min_val, max_val, A, B, l//2) + get_min_val(min_val, max_val, A, B, l//2 - 1))/2


A = [1, 4, 5]
B = [2,3]
A = [5,6,7,8,9]
B = [1,2]
# A = [1,2]
# B = [3,4]
print(findMedianSortedArrays(A, B))