'''
Given an string A. The only operation allowed is to insert characters in the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.



Input Format

The only argument given is string A.
Output Format

Return the minimum characters that are needed to be inserted to make the string a palindrome string.
For Example

Input 1:
    A = "ABC"
Output 1:
    2
    Explanation 1:
        Insert 'B' at beginning, string becomes: "BABC".
        Insert 'C' at beginning, string becomes: "CBABC".

Input 2:
    A = "AACECAAAA"
Output 2:
    2
    Explanation 2:
        Insert 'A' at beginning, string becomes: "AAACECAAAA".
        Insert 'A' at beginning, string becomes: "AAAACECAAAA".
'''


def solve(string):
    # O(N^2)
    # if string == string[::-1]:
    #     return 0
    # for i in range(1, len(string)):
    #     b = string[-1*i:][::-1] + string
    #     if b == b[::-1]:
    #         return i

    # O(N)
    if len(A) <= 1:
        return 0
    i, j, j_start = 0, len(A)-1, len(A)-1
    while i < j:
        if A[i] == A[j]:
            i += 1
            j -= 1
        else:
            j = j_start - 1
            j_start = j
            i = 0
    return len(A) - 1 - j_start


A = "ABC"
# A = "ACECAAAA"
# A = "eylfpbnpljvrvipyamyehwqnq"
print(solve(A))
