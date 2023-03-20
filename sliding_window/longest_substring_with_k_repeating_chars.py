"""
Given a string s and an integer k, return the length of the longest substring of s such that the
frequency of each character in this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
"""

"""
CAN BE SOLVED BETTER USING DAC RECURSION APPROACH
"""


def longestSubstring(s: str, k: int) -> int:
    longest_substring = 0  # variable to store the length of the longest substring that satisfies the condition
    for unique_chars in range(1, len(set(s)) + 1):  # loop over all possible numbers of unique characters in the string
        # Use a sliding window to check all substrings with "unique_chars (1 to ...)" unique characters
        left = 0  # left index of sliding window
        right = 0  # right index of sliding window
        count_unique_chars = 0  # number of unique characters in the sliding window
        count_at_least_k = 0  # number of characters that appear at least k times in the sliding window
        char_count = {}  # dictionary to store the count of each character in the sliding window
        while right < len(s):  # move the sliding window to the right until the right of the string
            if s[right] not in char_count:  # if s[right] is not already in the sliding window
                count_unique_chars += 1  # increment count_unique_chars
                char_count[s[right]] = 0  # initialize the count of s[right] to 0
            char_count[s[right]] += 1  # increment the count of s[right] in the sliding window
            if char_count[s[right]] == k:  # if s[right] appears k times in the sliding window
                count_at_least_k += 1  # increment count_at_least_k
            right += 1  # move the right index of the sliding window to the right
            while count_unique_chars > unique_chars:  # move the left index of the sliding window to the right until
                # the number of unique characters in the sliding window is equal to unique_chars
                char_count[s[left]] -= 1  # decrement the count of s[left] in the sliding window
                if char_count[s[left]] == k - 1:  # if s[left] appears k-1 times in the sliding window
                    count_at_least_k -= 1  # decrement count_at_least_k
                if char_count[s[left]] == 0:  # if the count of s[left] in the sliding window is 0
                    count_unique_chars -= 1  # decrement count_unique_chars
                    del char_count[s[left]]  # remove s[left] from char_count
                left += 1  # move the left index of the sliding window to the right
            if count_unique_chars == unique_chars and count_unique_chars == count_at_least_k:  # if the number of unique characters in the sliding window is equal to unique_chars and all characters in the sliding window appear at least k times
                longest_substring = max(longest_substring, right - left)  # update longest_substring if the length of the sliding window is greater than longest_substring
    return longest_substring  # return the length of the longest substring that satisfies the condition


print(longestSubstring("abcbddeffg", 2))
