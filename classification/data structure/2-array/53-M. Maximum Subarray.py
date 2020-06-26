#coding=utf-8

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 如果当前sum<0而且num<0, 就sum = 0
    # maxSum每次curSum更新后，都需要比较更新一次
    maxSum = nums[0]
    curSum = 0

    for num in nums:
        curSum += num
        maxSum = max(maxSum, curSum)

        if curSum < 0:
            curSum = max(0, num)
    return maxSum