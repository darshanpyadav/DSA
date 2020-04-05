'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result.
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input :
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]
'''


def merge(A, B):
    # O((m+n)log(m+n))
    # A.extend(B) -> O(n)
    # A.sort() -> O((m+n)log(m+n))
    # ******************************************************************************************************************
    if B[0] >= A[-1]:
        A.extend(B)
        print(' '.join(list(map(str, A))))
        return
    if B[-1] <= A[0]:
        B.extend(A)
        print(' '.join(list(map(str, B))))
        return
    # Like merge sort
    # Time: O(m+n)
    # Space: O(m+n)
    i, j = 0, 0
    sorted_list = []
    while len(sorted_list) <= len(A) + len(B):
        if A[i] < B[j]:
            sorted_list.append(A[i])
            i += 1
        else:
            sorted_list.append(B[j])
            j += 1
        if i == len(A):
            sorted_list.extend(B[j:])
            break
        if j == len(B):
            sorted_list.extend(A[i:])
            break

    print(' '.join(list(map(str, sorted_list))))
    # ******************************************************************************************************************


a = [1, 5, 8]
b = [6, 9]
merge(a, b)
