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
        longest_substring = max(longest_substring, right+1-left)
        return longest_substring


a = Solution()
print(a.lengthOfLongestSubstring("leviosa"))
print(a.lengthOfLongestSubstring("abracadabra"))
print(a.lengthOfLongestSubstring("pwwaakew"))
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("bbbbb"))
print(a.lengthOfLongestSubstring("tmmzuxt"))
print(a.lengthOfLongestSubstring("dvdf"))
