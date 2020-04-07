'''
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained ( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).

 Note: You may not slant the container.
Example :

Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3.
So total area = 3 * 2 = 6
'''


def maxArea(A):
    # O(N^2)
    # area = 0
    # n = len(A)
    # for i in range(n-1):
    #     for j in range(i+1, n):
    #         area = max(area, (j-i) * min(A[i], A[j]))
    # return area

    # O(N)
    # Front-end pointer
    area = 0
    start, end = 0, len(A)-1

    while start < end:
        area = max(area, min(A[start], A[end])*(end-start))
        if A[start] < A[end]:
            start += 1
        else:
            end -= 1
    return area


A = [1, 5, 4, 3]
A = [1]
A = [1,8,6,2,5,4,8,3,7]
print(maxArea(A))
