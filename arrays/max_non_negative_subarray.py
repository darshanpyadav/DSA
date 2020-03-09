import unittest


def maxset(A):
    cur_sum, max_sum = 0, float('-inf')
    start, end, previous_start = 0, 1, 0
    for i in range(len(A)):
        if A[i] < 0:
            if cur_sum > max_sum:
                previous_start, end = start, i
                max_sum = cur_sum
            cur_sum = 0
            start = i + 1
        else:
            cur_sum += A[i]
    if cur_sum > max_sum:
        return list(A[start:])
    return list(A[previous_start:end])


class TestInfixToPostfix(unittest.TestCase):
    def test(self):
        expressions = {(10, -1, 2, 3, -4, 100): [100],  (2, 3, 4, -1, -2, 1, 5, 6, 3): [1, 5, 6, 3],
                       (1, 0, 0, 1, -1, -1, 0, 0, 1, 0): [1, 0, 0, 1], (0, 0, -1, 0): [0, 0],
                       (-846930886, -1714636915, 424238335, -1649760492): [424238335]}
        results = [maxset(expression) for expression in expressions]
        self.assertListEqual(results, list(expressions.values()))


if __name__ == "__main__":
    unittest.main()

