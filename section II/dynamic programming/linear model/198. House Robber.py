def rob(nums):
    N = len(nums)
    if N == 0: return 0

    dp = [0]*(N+1)
    dp[1] = nums[0]
    for i in range(2, N+1):
        dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])

    return dp[-1]

nums = []
print(rob(nums))