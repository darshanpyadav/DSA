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
    if string == string[::-1]:
        return 0
    for i in range(1, len(string)):
        b = string[-1*i:][::-1] + string
        if b == b[::-1]:
            return i


A = "ABC"
# A = "ACECAAAA"
# A = "eylfpbnpljvrvipyamyehwqnq"
print(solve(A))
