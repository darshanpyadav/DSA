# The largest element bubbles up every cycle


def bubble_sort(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


print(bubble_sort([5, 3, 2, 4, 1]))


# T(N) = summation(n-1)
# T(N) = N^2/2 - N/2 = O(N^2)

# Best case: O(1)
# When elements are already sorted, no swaps

# Average, Worst case: O(N^2)