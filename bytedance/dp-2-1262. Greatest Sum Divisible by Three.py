def maxSumDivThree(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [0, 0, 0]
    for num in nums:
        for i in dp[:]:
            dp[(i + num) % 3] = max(i + num, dp[(i + num) % 3])
    return dp[0]