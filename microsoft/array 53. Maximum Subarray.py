#coding=utf-8
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