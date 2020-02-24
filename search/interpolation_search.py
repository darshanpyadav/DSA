def interpolation_search(l, ele):
    start = 0
    end = len(l) - 1

    while start <= end and l[start] <= ele <= l[end]:
        mid = start + int((end - start) * (ele - l[start]) / (l[end] - l[start]))
        if l[mid] == ele:
            return True
        elif l[mid] < ele:
            start = mid + 1
        else:
            end = mid - 1
    return False


print(interpolation_search([3, 5, 6, 8, 11, 12, 14, 15, 17, 18], 10))
