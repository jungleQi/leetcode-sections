'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def maxSubArray(nums):
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        max_sum = max(nums[i], max_sum)

    return max_sum

nums = [-1,0]
print(maxSubArray(nums))

