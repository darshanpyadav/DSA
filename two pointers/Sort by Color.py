'''
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
'''
from collections import defaultdict


def sortColors(A):
    d = defaultdict(lambda: 0)
    for i in A:
        d[i] += 1
    A = [0]*d[0] + [1]*d[1] + [2]*d[2]
    return A


A = [0, 1, 2, 0, 1, 2]
print(sortColors(A))
