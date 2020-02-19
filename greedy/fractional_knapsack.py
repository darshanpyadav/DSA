# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 29/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


def fractional_knapsack(values, weights, capacity):
    """Return maximum value of items

    max_value is returned where max_value is the maximum value of
    items with total weight not more than capacity.

    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.

    capacity is the maximum weight.
    """
    sorted_ratio = sorted(zip(values, weights), key=lambda el: el[0]/el[1], reverse=True)
    max_value = 0

    for v, w in sorted_ratio:
        if capacity >= w:
            max_value += v
            capacity -= w
        else:
            max_value += capacity*(v/w)
            break

    return max_value


if __name__ == "__main__":
    values = map(int, input("Enter values").split())
    weights = map(int, input("Enter weights").split())
    capacity = int(input("Enter capacity"))
    max_value = fractional_knapsack(values, weights, capacity)
    print(max_value)

# O(N*logN)