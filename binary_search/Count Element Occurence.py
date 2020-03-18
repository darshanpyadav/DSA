'''
Given a sorted array of integers, find the number of occurrences of a given target value.
Your algorithm’s runtime complexity must be in the order of O(log n).
If the target is not found in the array, return 0

**Example : **
Given [5, 7, 7, 8, 8, 10] and target value 8,
return 2.
'''


def findCount(A, B):
    n = len(A)
    count = 0
    start, end = 0, n - 1
    search_index = -1

    while start <= end:
        mid = (start+end)//2
        if A[mid] == B:
            count += 1
            search_index = mid
            break
        elif B < A[mid]:
            end = mid - 1
        else:
            start = mid + 1

    if search_index != -1:
        for i in range(search_index-1, -1, -1):
            if A[i] == B:
                count += 1

        for i in range(search_index+1, n):
            if A[i] == B:
                count += 1

    return count


# print(findCount([5,7,7,8,8,8,8,10], 8))
print(findCount([ 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10 ], 1))