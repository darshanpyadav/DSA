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
    n = len(A)
    combined_list = zip(A, range(n))
    combined_list = sorted(combined_list)

    # calculate prefix max index array
    max_index = [None]*n
    index = float('-inf')
    for i in range(n-1, -1, -1):
        index = max(index, combined_list[i][1])
        max_index[i] = index

    # calculate maximum j-i
    return max(max_index[i] - combined_list[i][1] for i in range(n))


print(maximumGap([3, 5, 4, 2]))