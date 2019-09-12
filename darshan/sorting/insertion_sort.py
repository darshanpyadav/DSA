import bisect


def insertion_sort(l):
    sorted_list = [l[0]]
    for i in range(len(l)-1):
        for j in range(len(sorted_list)):
            bisect.insort(sorted_list, l[i+1])
            break
    return sorted_list


print(insertion_sort([5, 3, 2, 4, 1]))


# Time complexity is O(N^2)