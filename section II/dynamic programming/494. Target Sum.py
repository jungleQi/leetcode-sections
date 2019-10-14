import sys
def findTargetSumWays(nums, S):
    N = len(nums)
    dp = [[0 for _ in range(2001)] for _ in range(N)]
    dp[0][nums[0]+1000] = 1
    dp[0][-nums[0]+1000] += 1
    for i in range(1,N):
        for sum in range(-1000, 1001):
            if dp[i-1][sum+1000] > 0:
                dp[i][sum+1000+nums[i]] += dp[i-1][sum+1000]
                dp[i][sum+1000-nums[i]] += dp[i-1][sum+1000]

    return 0 if S>1000 else dp[N-1][S+1000]


#nums = [2,20,24,38,44,21,45,48,30,48,14,9,21,10,46,46,12,48,12,38]
#S = 48
nums = [1, 1, 1, 1, 1]
S = 30000
print(findTargetSumWays(nums, S))