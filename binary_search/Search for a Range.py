'''
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].



Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

 Return an array of size 2, such that first element = starting position of B in A and second element = ending position
 of B in A, if B is not found in A return [-1, -1].
Constraints

1 <= N <= 10^6
1 <= A[i], B <= 10^9
For Example

Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]
'''


def searchRange(A, B):
    n = len(A)
    start, end = 0, n-1
    r = [-1, -1]

    while start <= end:
        mid = (start+end)//2

        if A[mid] == B:
            r[0] = r[1] = mid
            break
        elif A[mid] > B:
            end = mid - 1
        else:
            start = mid + 1

    if r[0] != -1:
        for i in range(r[0]-1, -1, -1):
            if A[i] == B:
                r[0] = i

        for i in range(r[0]+1, n):
            if A[i] == B:
                r[1] = i

    return r
# **********************************************************************************************************************
def searchRange(A, B):
    res = []
    def search(A, B, first=True):
        n = len(A)
        start, end = 0, n-1
        res = -1

        while start <= end:
            mid = (start+end)//2

            if A[mid] == B:
                res = mid
                if first:
                    end = mid - 1
                else:
                    start = mid + 1
            elif A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1

        return res

    res.append(search(A, B))
    res.append(search(A, B, False))

    return res


print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 17, 100, 111], 3))
