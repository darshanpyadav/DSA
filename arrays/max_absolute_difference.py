'''
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
'''


from itertools import combinations


def max_difference(A):
    return max(abs(A[x-1]-A[y-1]) + abs(x-y) for x, y in combinations(range(1, len(A)+1), 2))
# ************************************************************************************************


# def get_number_of_combinations(n):
#     if n == 2:
#         return 1
#     return (n-1) + get_number_of_combinations(n-1)
def get_number_of_combinations(n):
    a = {2: 1}
    for i in range(3, n+1):
        a[i] = a[i-1] + (i-1)
    return a[n]


def max_difference(A):
    n = get_number_of_combinations(len(A))
    count, x, y = 0, 1, 2
    max_difference = 0
    # print(n)

    x_in, y_in = x, y
    while count < n:
        # print(x_in, y_in)
        d = abs(A[x_in-1]-A[y_in-1]) + abs(x_in-y_in)
        max_difference = d if d > max_difference else max_difference
        if y_in >= len(A):
            x, y = x+1, y+1
            x_in, y_in = x, y
        else:
            y_in += 1
        count += 1
    return max_difference
# ************************************************************************************************
'''
    f(i, j) = |A[i] - A[j]| + |i - j|
    can be written in 4 ways
    (A[i] + i) - (A[j] + j)
    or
    (A[i] - i) - (A[j] - j) 
    or
    -(A[i] - i) + (A[j] - j )
    or 
    -(A[i] + i) + (A[j] + j)
    
    (A[i] + i) - (A[j] + j) == -(A[i] + i) + (A[j] + j)
    (A[i] - i) - (A[j] - j) == -(A[i] - i) + (A[j] - j )
'''


# O(N)
def max_difference(A):
    # create two arrays
    # for one you add index to the ele
    # for another you subtract index from ele
    a = []
    b = []
    for i, val in enumerate(A):
        a.append(val+i)
        b.append(val-i)
    # to maximise the sum, you'll find difference of max and min elements of each
    max1, min1 = (max(a), min(a))
    max2, min2 = (max(b), min(b))

    return max(abs(max1 - min1), abs(max2 - min2))


# print(max_difference([2, 2, 2]))
# print(max_difference([1, 3, -1, 3]))
print(max_difference([55, -8, 43, 52, 8, 59, -91, -79, -18, -94]))
