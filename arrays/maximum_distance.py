'''
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].

If there is no solution possible, return -1.

Example :

A : [3 5 4 2]

Output : 2
for the pair (3, 4)

'''


from itertools import combinations


# def maximumGap(A):
    # O(N^2)
    # max_distance = -1
    # for i in range(len(A)):
    #     for j in range(i+1, len(A)):
    #         if A[j] >= A[i]:
    #             max_distance = max(max_distance, j-i)
    #
    # return max_distance

# *****************************************************************************
def maximumGap(A):
    max_distance = 0
    for i in combinations(range(len(A)), 2):
        if A[i[1]] >= A[i[0]]:
            max_distance = max(max_distance, i[1]-i[0])
    return max_distance

# *****************************************************************************


def maximumGap(A):
    array = list(range(len(A)))
    array.sort(key=lambda i: A[i])
    max_gap = 0
    current_min = array[0]
    for i in array:
        if i < current_min:
            current_min = i
        else:
            max_gap = max(max_gap, i - current_min)
    return max_gap


print(maximumGap([3, 5, 4, 2]))
