# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 15/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


def divide(l):
    mid = len(l)//2
    return l[:mid], l[mid:]


def find_max(min1, max1, min2, max2):
    return min1 if min1 < min2 else min2, max1 if max1 > max2 else max2


def min_max(l):
    if len(l) > 1:
        first_list, second_list = divide(l)
        min1, max1 = min_max(first_list)
        min2, max2 = min_max(second_list)
        return find_max(min1, max1, min2, max2)
    else:
        return l[0], l[0]


print(min_max([4, 0, 123, 5]))


# O(n)