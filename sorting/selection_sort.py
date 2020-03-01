# Improves bubble sort by making only one exchange per pass


def selection_sort(l):
    for i in range(len(l)-1, 0, -1):
        max_index = i
        for j in range(i):
            if l[j] > l[max_index]:
                max_index = j
        l[max_index], l[i] = l[i], l[max_index]
    return l


# def selection_sort(l):
#     for i in range(len(l)):
#         min_index = i
#         for j in range(i, len(l)):
#             if l[j] < l[min_index]:
#                 min_index = j
#         if min_index != i:
#             l[i], l[min_index] = l[min_index], l[i]
#     return l


print(selection_sort([5, 3, 2, 4, 1]))


# T(N) = summation(n-1)
# T(N) = N^2/2 - N/2 = O(N^2)

# Best, Average, Worst case: O(N^2)
# Space: O(1)
# Sorting in Place: Yes
# Stable: No, can be made stable by inserting min ele at i, than swapping at i

# Faster than bubble sort as it involves less swaps
