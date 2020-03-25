'''
Implement strStr().

 strstr - locate a substring ( needle ) in a string ( haystack ).
Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases.
'''


def strStr(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


A = "bbbbbbbbab"
B = "baba"
A = "bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba"
B = "babaaa"
print(strStr(A, B))
