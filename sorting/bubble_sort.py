# The largest element bubbles up every cycle


def bubble_sort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


print(bubble_sort([5, 3, 2, 4, 1]))


def bubble_sort_optimized(l):
    for i in range(len(l) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if l[j] > l[j + 1]:
                swapped = True
                l[j], l[j + 1] = l[j + 1]
        if not swapped:
            return l
    return l


# T(N) = summation(n-1)
# T(N) = N^2/2 - N/2 = O(N^2)

# Best case: O(N) -> with optimized implementation, can be stopped after one loop
# Average, Worst case: O(N^2)
# Space: O(1)
# Sorting in Place: Yes
# Stable: Yes
