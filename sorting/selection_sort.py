# Improves bubble sort by making only one exchange per pass


def selection_sort(l):
    for i in range(len(l)-1, 0, -1):
        max_index = i
        for j in range(i):
            if l[j] > l[max_index]:
                max_index = j
        l[max_index], l[i] = l[i], l[max_index]
    return l


print(selection_sort([5, 3, 2, 4, 1]))


# T(N) = summation(n-1)
# T(N) = N^2/2 - N/2 = O(N^2)

# Best case: O(1)
# When elements are already sorted, no swaps

# Average, Worst case: O(N^2)

# Faster than bubble sort as it involves less swaps