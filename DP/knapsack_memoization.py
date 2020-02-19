# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 24/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************
import numpy as np
import timeit


def knapsack(weights, values, limit):
    """Return the maximum value of items that doesn't exceed limit.

    value[i] is the value of item i and weight[i] is the weight of item i
    for 1 <= i <= n where n is the number of items.

    limit is the maximum weight.
    """
    n = len(weights) - 1
    m = [[-1]*(limit+1) for _ in range(n + 1)]

    # m[i][w] will store the maximum value that can be attained with a maximum
    # limit of w and using only the first i items
    return knapsack_helper(weights, values, limit, n, m), m


def knapsack_helper(weights, values, w, i, m):
    """Return maximum value of first i items attainable with weight <= w.

    m[i][w] will store the maximum value that can be attained with a maximum
    limit of w and using only the first i items
    This function fills m as smaller subproblems needed to compute m[i][w] are
    solved.

    value[i] is the value of item i and weight[i] is the weight of item i
    for 1 <= i <= n where n is the number of items.
    """
    if m[i][w] >= 0:
        return m[i][w]
    if i == 0:
        m[i][w] = 0
    else:
        if weights[i] > w:
            m[i][w] = knapsack_helper(weights, values, w, i-1, m)
        else:
            # the best subset of m[i-1] with weight at most w or
            # the best subset of m[i-1] with weight at most w-w[i] plus item v[i]
            m[i][w] = max(knapsack_helper(weights, values, w, i-1, m),
                          knapsack_helper(weights, values, w-weights[i], i-1, m) + values[i])
    return m[i][w]


if __name__ == "__main__":
    # values = list(map(int, input("Values:").split()))
    # weights = list(map(int, input("Weights:").split()))
    # limit = int(input("Enter the limit"))
    values = [10, 5, 20, 40, 30]
    weights = [4, 1, 10, 20, 7]
    limit = 10
    # answer, m = knapsack(weights, values, limit)
    # print(answer)
    # print(np.matrix(m))
    print("**************MEMOIZATION*************")
    print(timeit.repeat("knapsack([4, 1, 10, 20, 7], [10, 5, 20, 40, 30], 10)",
                        "from darshan.DP.knapsack_memoization import knapsack", number=10000))
    print("**************BOTTOM UP*************")
    print(timeit.repeat("knapsack([4, 1, 10, 20, 7], [10, 5, 20, 40, 30], 10)",
                        "from darshan.DP.knapsack_bottom_up import knapsack", number=10000))
