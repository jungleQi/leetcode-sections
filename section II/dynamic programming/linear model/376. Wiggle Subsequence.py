def wiggleMaxLength(nums):
    N = len(nums)
    dp = [[1 for _ in range(2)] for _ in range(N)]
    for i in range(1,N):
        if nums[i]-nums[i-1]>0:
            dp[i][1] = dp[i-1][0]+1
            dp[i][0] = dp[i-1][0]
        elif nums[i]-nums[i-1]<0:
            dp[i][0] = dp[i-1][1]+1
            dp[i][1] = dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]

    return max(dp[-1][0], dp[-1][1])

nums = [1]
print(wiggleMaxLength(nums))