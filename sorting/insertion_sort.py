def insertion_sort(l):
    for i in range(1, len(l)):
        ele = l[i]
        while ele < l[i-1] and i > 0:
            l[i] = l[i-1]
            i -= 1
        l[i] = ele
    return l


print(insertion_sort([5, 3, 2, 4, 1]))


# Best case: O(N)
# Average, Worst case: O(N^2)
# Space: O(1)
# Sorting in Place: Yes
# Stable: Yes
# Time complexity is O(N^2)