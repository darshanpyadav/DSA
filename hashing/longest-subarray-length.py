def solve(A):
    n = len(A)
    slow = fast = 0
    zeroes = ones = 0
    max_len = 0

    while slow < n and fast < n:
        if A[fast] == 1:
            ones += 1
        else:
            zeroes += 1
        if ones < zeroes:
            fast += 1
        else:
            if ones - zeroes == 1:
                max_len = max(max_len, fast-slow)
            if ones - zeroes > 1:
                if A[slow] == 0:
                    zeroes -= 1
                else:
                    ones -= 1
                slow += 1
    return max_len



# print(solve([0, 1, 1, 0, 0, 1]))
# print(solve([1, 0, 0, 1, 0]))
# print(solve([0, 0, 0, 0, 0]))
# print(solve([1, 1, 1, 1, 1, 1, 1]))
print(solve([0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]))