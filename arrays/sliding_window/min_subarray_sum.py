"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

"A subarray is a contiguous non-empty sequence of elements within an array."


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

import math
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        min_len = math.inf
        left = 0

        # move right always
        # move left only when the cur_sum >= target
        # window type: dynamic
        # window size = (right-left)
        for right, val in enumerate(nums):
            cur_sum += val

            # move until cur_sum is less than target
            while cur_sum >= target:
                min_len = min(min_len, right + 1 - left)
                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != math.inf else 0


a = Solution()
print(a.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(a.minSubArrayLen(4, [1, 4, 4]))
print(a.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(a.minSubArrayLen(12, [1, 2, 3, 4, 5]))
