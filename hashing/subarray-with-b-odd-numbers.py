def solve(A, B):
    n = len(A)
    count = 0
    prefix = [0] * (n + 1)
    odd = 0
    # traverse in the array
    for i in range(n):
        prefix[odd] += 1
        # if array element is odd
        if A[i] & 1:
            odd += 1

        # when number of odd elements>=M
        if odd >= B:
            count += prefix[odd - B]
    return count


print(solve([4, 3, 2, 3, 4], 2))
