"""
Given a string s, find the length of the longest
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

import math


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # track elements that have appeared
        ele_tracker = {}
        right = left = 0
        longest_substring = -math.inf

        # move right always
        # move left only when the val occurs again in the window, it is set to index of val + 1
        # window type: dynamic
        # window size = (right-left)
        for right, val in enumerate(s):
            # if value has already appeared
            # if appeared value is within the current sliding window
            if val in ele_tracker and (left <= ele_tracker[val] < right):
                # find the longest substring
                longest_substring = max(longest_substring, right-left)
                # move left to the element after the re-occurrence of the value
                left = ele_tracker[val] + 1
            ele_tracker[val] = right
        # For last iteration
        longest_substring = max(longest_substring, right + 1 - left)
        return longest_substring


# Others from leetcode
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         left = 0
#         seen = {}
#         output = 0
#
#         for right, curr in enumerate(s):
#             if curr in seen:
#                 left = max(left, seen[curr] + 1)
#             output = max(output, right - left + 1)
#             seen[curr] = right
#
#         return output

a = Solution()
print(a.lengthOfLongestSubstring("leviosa"))
print(a.lengthOfLongestSubstring("abracadabra"))
print(a.lengthOfLongestSubstring("pwwaakew"))
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("bbbbb"))
print(a.lengthOfLongestSubstring("tmmzuxt"))
print(a.lengthOfLongestSubstring("dvdf"))


class Solution1:
    def LongestSubstring(self, s: str) -> str:
        if not s:
            return 0

        # track elements that have appeared
        ele_tracker = {}
        right = left = 0
        longest_substring = ""

        # move right always
        # move left only when the val occurs again in the window, it is set to index of val + 1
        # window type: dynamic
        # window size = (right-left)
        for right, val in enumerate(s):
            # if value has already appeared
            # if appeared value is within the current sliding window
            if val in ele_tracker and (left <= ele_tracker[val] < right):
                # find the longest substring
                if right - left > len(longest_substring):
                    longest_substring = s[left: right + 1]
                # move left to the element after the re-occurrence of the value
                left = ele_tracker[val] + 1
            ele_tracker[val] = right
        # For last iteration
        if right + 1 - left > len(longest_substring):
            longest_substring = s[left: right + 1]
        return longest_substring


a = Solution1()
print(a.LongestSubstring("leviosa"))
print(a.LongestSubstring("abracadabra"))
print(a.LongestSubstring("pwwaakew"))
print(a.LongestSubstring("abcabcbb"))
print(a.LongestSubstring("bbbbb"))
print(a.LongestSubstring("tmmzuxt"))
print(a.LongestSubstring("dvdf"))
