'''
Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
and S2.

For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".



Input Format

The only argument given is an array of strings A.
Output Format

Return longest common prefix of all strings in A.
For Example

Input 1:
    A = ["abcdefgh", "aefghijk", "abcefgh"]
Output 1:
    "a"
    Explanation 1:
        Longest common prefix of all the strings is "a".

Input 2:
    A = ["abab", "ab", "abcd"];
Output 2:
    "ab"
    Explanation 2:
        Longest common prefix of all the strings is "ab".
'''


def longestCommonPrefix(arr):
    # O(N^2)
    smallest_str = arr[0]
    for i in arr:
        if len(i) < len(smallest_str):
            smallest_str = i

    for i in range(len(smallest_str)):
        for j in arr:
            if not j.startswith(smallest_str[:i+1]):
                return smallest_str[:i]
    return smallest_str

# **********************************************************************************************************************


def longestCommonPrefix(S):
    # O(N)
    # min and max will give lexicographic min and max, so compare with min and max
    word1 = min(S)
    word2 = max(S)

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            return word1[:i]
    return word1


A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abcdefgh", "aefghijk", "abc"]
# A = ["abab", "ab", "abcd"]
# A = [ "abcd", "abcd", "efgh" ]
# A = ["abc", "abc", "abc"]
print(longestCommonPrefix(A))
