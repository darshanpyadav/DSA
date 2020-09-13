'''You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1
1 occurs 3 times which is more than 5/3 times. '''


def repeatedNumber(nums):

    count1 = count2 = 0
    first = second = float('inf')
    target = len(nums) / 3

    for num in nums:
        if first == num:
            count1 += 1
        elif second == num:
            count2 += 1
        elif count1 == 0:
            count1 += 1
            first = num
        elif count2 == 0:
            count2 += 1
            second = num
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0

    for num in nums:
        if num == first:
            count1 += 1
        elif num == second:
            count2 += 1

    return first if (count1 > target) else second if (count2 > target) else -1


print(repeatedNumber([1, 2, 3, 1, 1]))
