# *****************************************************************************
# Author            : darshanp (darshanp@juniper.net)
# Date              : 24/09/19
# Last modified by  : darshanp
# Version           : 1.0
# Description       : Let-s-do-it
# *****************************************************************************


def knapsack(weights, values, limit):
    n = len(weights) - 1
    m = [[-1]*(limit+1) for _ in range(n+1)]

    for w in range(limit + 1):
        m[0][w] = 0

    for i in range(1, n+1):
        for w in range(limit+1):
            if weights[i] > w:
                m[i][w] = m[i-1][w]
            else:
                m[i][w] = max(m[i-1][w], m[i-1][w-weights[i]] + values[i])

    return m[n][limit]


if __name__ == "__main__":
    # values = list(map(int, input("Values:").split()))
    # weights = list(map(int, input("Weights:").split()))
    # limit = int(input("Enter the limit"))
    values = [10, 5, 20, 40, 30]
    weights = [4, 1, 10, 20, 7]
    limit = 10
    print(knapsack(weights, values, limit))
