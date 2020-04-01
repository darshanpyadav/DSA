'''
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[i...j] where 0 <= i <= j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Example :

Input : "aaaabaaa"
Output : "aaabaaa"
'''


def longestPalindrome(A):
    # O(N^3)
    longest = ""
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i:j+1] == A[i:j+1][::-1]:
                if len(A[i:j+1]) > len(longest):
                    longest = A[i:j+1]
    return longest


print(longestPalindrome("abb"))
# print(longestPalindrome("abbcccbbbcaaccbababcbcabca"))