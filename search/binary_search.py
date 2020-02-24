def binary_search_iterative(l, item):
    first = 0
    last = len(l)-1
    while first <= last:
        mid = (first + last)//2
        if item == l[mid]:
            return True
        elif item < l[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False
# O(logN)


# Not recommended as slicing is again an O(K) operation
def binary_search_recursive(l, item):
    if len(l) == 0:
        return False
    mid = len(l) // 2
    if item == l[mid]:
        return True
    elif item < l[mid]:
        return binary_search_recursive(l[:mid], item)
    else:
        return binary_search_recursive(l[mid:], item)


binary_search_recursive([3, 5, 6, 8, 11, 12, 14, 15, 17, 18], 8)
