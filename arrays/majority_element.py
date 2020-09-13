'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''


def majority_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = None
    count = 0
    for num in nums:
        if count == 0:
            result = num
        if result == num:
            count += 1
        else:
            count -= 1
    return result


def is_majority(nums, ele):
    count = 0
    for num in nums:
        if num == ele:
            count += 1

    return True if count > len(nums) / 2 else False


if __name__ == "__main__":
    # assert Solution().majorityElement([1, 2, 2, 3, 3, 3, 3]) == 3
    # assert Solution().majorityElement([3, 3, 3, 3, 1, 1, 2]) == 3
    get_majority_ele = majority_element([4, 4, 4, 2, 4, 4, 4, 1, 1, 1, 1])
    print(get_majority_ele)
    is_majority = is_majority([4, 4, 4, 2, 4, 4, 4, 1, 1, 1, 1], get_majority_ele)
    print(is_majority)
