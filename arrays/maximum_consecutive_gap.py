''''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Example :

Input : [1, 10, 5]
Output : 5
Return 0 if the array contains less than 2 elements.

You may assume that all the elements in the array are non-negative integers and fit in the 32-bit signed integer range.
You may also assume that the difference will not overflow.
'''
import math


def maximumGap(A):
    n = len(A)

    if n < 2:
        return 0

    min_ele = min(A)
    max_ele = max(A)

    if min_ele == max_ele:
        return 0

    if n == 2:
        return max_ele - min_ele

    # for n-1 buckets
    buckets = [[] for _ in range(n-1)]
    bucket_size = (max_ele - min_ele) / (n-1)

    # put remaining n-2 numbers in buckets
    for number in A:
        if number != min_ele and number != max_ele:
            num = int(math.floor((number - min_ele) / bucket_size))
            buckets[num].append(number)

    # get only non-empty buckets
    non_empty_buckets = []
    for bucket in buckets:
        if bucket:
            non_empty_buckets.append(bucket)

    if not non_empty_buckets:
        return max_ele - min_ele
            
    max_gap = max(min(non_empty_buckets[0]) - min_ele, max_ele - max(non_empty_buckets[-1]))
    for i in range(1, len(non_empty_buckets)):
        gap = min(non_empty_buckets[i]) - max(non_empty_buckets[i-1])
        if gap > max_gap:
            max_gap = gap

    return max_gap


# print(maximumGap([5, 6, 4, 1, 2]))
# print(maximumGap([1, 10, 5]))
# print(maximumGap([ 100, 100, 100, 100, 100 ]))
print(maximumGap([ 1, 1, 2 ]))