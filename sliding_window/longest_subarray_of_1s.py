"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

import math
from typing import List


class Solution:
    # move right always
    # move left only when the number of 0s in window is > 1
    # window type: dynamic
    # window size = (right-left)
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        left = 0
        max_len = -math.inf

        for right, val in enumerate(nums):
            if not val:
                zero_count += 1
            while zero_count > 1 and left < right:
                if not nums[left]:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, right - left)
        return max_len


a = Solution()
print(a.longestSubarray([1, 1, 0, 1]))
print(a.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(a.longestSubarray([0, 0, 0, 0, 1]))
print(a.longestSubarray([1, 0, 0, 0, 0]))
print(a.longestSubarray([1, 0, 1, 0, 1, 0]))


"""
Longest Subarray of 1's After Deleting One Element
Constrained Subsequence Sum
Number of Substrings Containing All Three Characters
Count Number of Nice Subarrays
Replace the Substring for Balanced String
Max Consecutive Ones III
Binary Subarrays With Sum
Subarrays with K Different Integers
Fruit Into Baskets
Shortest Subarray with Sum at Least K
Minimum Size Subarray Sum
"""