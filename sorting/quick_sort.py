def quick_sort(l, start, end):
    if start < end:
        p = partition(l, start, end)
        quick_sort(l, start, p)
        quick_sort(l, p + 1, end)


def partition(l, start, end):
    pivot = l[start]
    i = start + 1
    j = end - 1
    while True:
        while i <= j and l[i] <= pivot:
            i += 1
        while i <= j and l[j] >= pivot:
            j -= 1

        if i <= j:
            l[i], l[j] = l[j], l[i]
        else:
            l[start], l[j] = l[j], l[start]
            return j


l = [5, 3, 2, 4, 1]
quick_sort(l, 0, len(l))
print(l)


# Best, Average Time complexity = O(N*logN)
# Worst Time complexity = O(N^2)
# Space: O(N*LogN)
