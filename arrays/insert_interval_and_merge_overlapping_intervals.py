'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.
'''


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def insert(intervals, new_interval):
    res = []
    intervals = intervals.append(new_interval)
    sorted_intervals = sorted(intervals, key=lambda x: x.start)
    res.append(sorted_intervals[0])

    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i].start < res[-1].end:
            res[-1].end = max(res[-1].end, sorted_intervals[i].end)
        else:
            res.append(sorted_intervals[i])

    return res
