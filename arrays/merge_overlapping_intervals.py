def merge(intervals):
    # Time: O(N*logN)
    # Space: O(1)

    res = []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    res.append(sorted_intervals[0])

    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], sorted_intervals[i][1])
        else:
            res.append(sorted_intervals[i])
    
    return res


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[6, 8], [1, 9], [2, 4], [4, 7]]))
