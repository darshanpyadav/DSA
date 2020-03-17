'''
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

Example :

Input 1:

A = [1, 3, 2, 4, 5]

Return: [1, 2]

Input 2:

A = [1, 2, 3, 4, 5]

Return: [-1]
In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
'''

def subUnsort(arr):
    n = len(arr)
    s, e = -1, -1

    for i in range(1, n):
        if arr[i-1] > arr[i]:
            s = i-1
            break

    if s == -1:
        return [-1]

    for i in range(n - 1, -1, -1):
        if arr[i-1] > arr[i]:
            e = i
            break

    min_unsorted, max_unsorted = min(arr[s:]), max(arr[s:e + 1])

    for i in range(s):
        if arr[i] > min_unsorted:
            s = i
            break

    for i in range(n - 1, e, -1):
        if arr[i] < max_unsorted:
            e = i
            break

    return [s, e]


# print(subUnsort([ 1, 2, 3 ]))
# print(subUnsort([1, 3, 2, 4, 5]))
# print(subUnsort([1, 2, 2, 3, 3, 5, 6, 6, 14, 17, 18, 17, 18, 15, 15, 17, 19, 14, 19, 18]))
# print(subUnsort([20, 1, 2, 2, 3, 3, 5, 6, 6, 14, 17, 18, 17, 18, 15, 15, 17, 19, 14, 19, 18]))
# print(subUnsort([ 4, 15, 4, 4, 15, 18, 20 ]))
# print(subUnsort([1, 4, 1, 2, 3]))
# print(subUnsort( [1, 2, 3 ]))