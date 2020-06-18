#coding=utf-8

def maxSumDivThree(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [0, 0, 0]
    for num in nums:
        #dp[:] 是关键，不然一个元素被处理之后，会被接着复用
        for i in dp[:]:
            dp[(i + num) % 3] = max(i + num, dp[(i + num) % 3])
    return dp[0]