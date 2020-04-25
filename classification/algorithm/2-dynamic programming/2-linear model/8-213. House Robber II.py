'''
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
'''

def rob(nums):
    def _rob(nums):
        ppn, pn = 0, 0
        for num in nums:
            n = max(ppn + num, pn)
            ppn, pn = pn, n
        return pn

    if not nums: return 0
    return max(_rob(nums[:-1]), _rob(nums[1:]), nums[0])


nums = [1,2,3]
print(rob(nums))