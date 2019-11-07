'''
Given an integer array nums, find the contiguous subarray (containing at least one number)
 which has the largest sum and return its sum.
'''

def maxSubArray(nums):
    maxSum, curSum = nums[0],0

    for num in nums:
        curSum += num
        if curSum > 0:
            maxSum = max(maxSum, curSum)
        else:
            curSum = num if num >= 0 else 0
            maxSum = max(maxSum, num)

    return maxSum


nums = [-3,2,-1,1]
print(maxSubArray(nums))