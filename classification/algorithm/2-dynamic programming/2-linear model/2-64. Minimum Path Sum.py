def maxProduct(nums):
    N = len(nums)
    dp = [[nums[i],nums[i]] for i in range(N)]

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
        dp[i][1] = max(dp[i-1][0]*nums[i], dp[i-1][1]*nums[i], nums[i])
    return max([item[1] for item in dp])

nums = [2,3,-2,4,0,2,-1,-1,4,-2,1,4,-2,-3]
print(maxProduct(nums))