'''
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
'''


# def wave(A):
#     # O(NlongN)
#     # A = sorted(A)
#     # j = 1
#     # while j < len(A):
#     #     A[j-1], A[j] = A[j], A[j-1]
#     #     j += 2
#     # return A

def wave(A):
    # O(N)
    j = 1
    while j < len(A):
        if A[j-1] < A[j]:
            A[j-1], A[j] = A[j], A[j-1]
        if j + 1 < len(A):
            if A[j+1] < A[j]:
                A[j+1], A[j] = A[j], A[j+1]
        j += 2
    return A


print(wave([10, 5, 6, 3, 2, 20, 100, 80]))
print(wave([20, 10, 8, 6, 4, 2]))