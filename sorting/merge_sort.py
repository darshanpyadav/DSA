def divide(l):
    mid = len(l)//2
    return l[:mid], l[mid:]


def merge_sorted_lists(left_list, right_list):
    if not len(left_list):
        return right_list
    if not len(right_list):
        return left_list
    merged_list = []
    i, j = 0, 0
    while len(merged_list) <= len(left_list) + len(right_list):
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1
        if i == len(left_list):
            merged_list.extend(right_list[j:])
            break
        if j == len(right_list):
            merged_list.extend(left_list[i:])
            break
    return merged_list


def merge_sort(l):
    if len(l) <= 1:
        return l
    first_half, second_half = divide(l)
    return merge_sorted_lists(merge_sort(first_half), merge_sort(second_half))


print(merge_sort([5, 3, 2, 4, 1]))


# Best, Worst, Average Time complexity = O(N*logN)
# Space: O(N)