'''
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;
Example :

Input :
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5
         With 10 from A, 15 from B and 10 from C.
'''


def minimize(A, B, C):
    min_diff = float('inf')
    indices = [len(A)-1, len(B)-1, len(C)-1]
    while indices[0] >= 0 and indices[1] >= 0 and indices[2] >= 0:
        a, b, c = A[indices[0]], B[indices[1]], C[indices[2]]
        max_ele = max((a, 0), (b, 1), (c, 2))
        diff = abs(max(a, b, c) - min(a, b, c))
        if diff == 0:
            return 0
        if diff < min_diff:
            min_diff = diff
        indices[max_ele[1]] -= 1
    return min_diff


A = [1,4,10]
B = [2, 15, 20]
C = [10, 12]
print(minimize(A,B,C))
