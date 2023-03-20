"""
Find the longest substring of a string containing `k` distinct characters
Google Translate Icon
Given a string and a positive number k, find the longest substring of the string containing k distinct characters.
If k is more than the total number of distinct characters in the string, return the whole string.

The problem differs from the problem of finding the longest subsequence with k distinct characters.
Unlike subsequences, substrings are required to occupy consecutive positions within the original string.


For example, consider string abcbbbbbbbdbdbbdcdabd.

For k = 2, o/p is ‘bbbbbbbdbdbbd’
"""

import math


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # if k > distinct chars in s, return -1
        if not s:
            return 0

        if len(set(s)) < k:
            return -1

        # track letters
        char_tracker = {}
        longest_substring = -math.inf
        left = 0

        # move right always
        # track elements count
        # window type: dynamic
        # window size = (right-left)
        # move left when the distinct elements are greater than k until:
        #       one element is completely eliminated (by tracking it's occurrences)
        for right, val in enumerate(s):
            # increase occurrence count by 1
            if val in char_tracker:
                char_tracker[val] += 1
            else:
                char_tracker[val] = 1

            # completely eliminate one distinct character before moving onto next
            while len(char_tracker) > k:
                left_char = s[left]
                if char_tracker[left_char] > 1:
                    char_tracker[left_char] -= 1
                else:
                    char_tracker.pop(left_char)
                left += 1
            longest_substring = max(longest_substring, right - left)

        return longest_substring


a = Solution()
print(a.length_of_longest_substring_k_distinct("abcbdbdbbdcdabd", 1))
print(a.length_of_longest_substring_k_distinct("abcbdbdbbdcdabd", 2))
print(a.length_of_longest_substring_k_distinct("abcbdbdbbdcdabd", 3))
print(a.length_of_longest_substring_k_distinct("abcbdbdbbdcdabd", 4))
print(a.length_of_longest_substring_k_distinct("eceba", 2))
print(a.length_of_longest_substring_k_distinct("eceba", 3))
print(a.length_of_longest_substring_k_distinct("eceba", 4))
print(a.length_of_longest_substring_k_distinct("WORLD", 2))
print(a.length_of_longest_substring_k_distinct("WORLD", 3))
print(a.length_of_longest_substring_k_distinct("WORLD", 4))
print(a.length_of_longest_substring_k_distinct("gbwkfnqduxwfn", 15))


class Solution1:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def longest_substring_k_distinct(self, s: str, k: int) -> int:
        # if k > distinct chars in s, return -1
        if not s:
            return 0

        if len(set(s)) < k:
            return -1

        # track letters that
        char_tracker = {}
        longest_substring = ""
        left = 0

        for right, val in enumerate(s):
            # increase occurrence count by 1
            if val in char_tracker:
                char_tracker[val] += 1
            else:
                char_tracker[val] = 1

            # completely eliminate one distinct character before moving onto next
            while len(char_tracker) > k:
                left_char = s[left]
                if char_tracker[left_char] > 1:
                    char_tracker[left_char] -= 1
                else:
                    char_tracker.pop(left_char)
                left += 1
            if (right - left) > len(longest_substring):
                longest_substring = s[left:right+1]

        return longest_substring


        # Initial solution that timed out
        #
        # char_tracker = {}
        # longest_substring = ""
        # left = right = 0
        #
        # for right, val in enumerate(s):
        #     char_tracker[val] = right
        #     if len(char_tracker) > k:
        #         if (right - left) > len(longest_substring):
        #             longest_substring = s[left:right]
        #         min_char = min(char_tracker.items(), key=lambda l: l[1])
        #         left = min_char[1] + 1
        #         char_tracker.pop(min_char[0])
        # if (right + 1 - left) > len(longest_substring):
        #     longest_substring = s[left:right]
        #
        # return longest_substring


a = Solution1()
print(a.longest_substring_k_distinct("abcbdbdbbdcdabd", 2))
print(a.longest_substring_k_distinct("abcbdbdbbdcdabd", 3))
print(a.longest_substring_k_distinct("abcbdbdbbdcdabd", 4))
print(a.longest_substring_k_distinct("eceba", 2))
print(a.longest_substring_k_distinct("eceba", 3))
print(a.longest_substring_k_distinct("eceba", 4))
print(a.longest_substring_k_distinct("WORLD", 2))
print(a.longest_substring_k_distinct("WORLD", 3))
print(a.longest_substring_k_distinct("WORLD", 4))

# class Solution:
#
#     def longestKSubstr(self, String, K):
#         '''
#             This method finds the longest substring with at most K
#             Distinct characters.
#             input: string and a number k
#             output: longest substring that has at most k distinct characters
#         '''
#         if len(set(s)) < k:
#             return -1
#         # define a dictionary that will work as hash table to hold our
#         # characters and their frequencies.
#         table = dict()
#
#         # two variables will point to the start and end of the window
#         start, end = 0, 0
#
#         # variable to hold the size of the longest substring
#         longest = 0
#
#         # expand the window
#         for end in range(len(String)):
#             # get the new character
#             newCharacter = String[end]
#
#             # add the new character in the hash table
#             if newCharacter in table.keys():
#                 table[newCharacter] += 1
#             else:
#                 table[newCharacter] = 1
#
#             # check if number of distinct characters in window is more
#             # than K
#             while len(table) > K:
#                 startCharacter = String[start]
#                 start += 1
#                 table[startCharacter] -= 1
#                 # if frequency becomes 0 then remove the character
#                 if table[startCharacter] == 0:
#                     table.pop(startCharacter)
#
#             # check if current window is greatest seen so far
#             if (end - start + 1 > longest):
#                 longest = end - start + 1
#
#         return longest
