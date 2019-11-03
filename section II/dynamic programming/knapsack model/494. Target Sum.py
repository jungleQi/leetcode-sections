import sys

#2D: if S is very big，causing Memory Limit Exceeded
def findTargetSumWays_2d_knapsack(nums,S):
    target,mod = divmod(sum(nums)+S, 2)
    if mod != 0: return 0

    N = len(nums)
    dp = [[0 for _ in range(target+1)] for _ in range(1+N)]

    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(target+1):
            if nums[i-1]<=j:
                dp[i][j] = dp[i-1][j-nums[i-1]]+ dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

#1D : reversely traverse from target to num-1
#1D hardly reduce the time consume than 2D
def findTargetSumWays(nums, S):
    total = sum(nums)
    if total < S: return 0
    if (total + S) & 1: return 0
    target = (total + S) / 2

    dp = [0] * (target + 1)
    dp[0] = 1

    for num in nums:
        for val in range(target, num - 1, -1):
            if dp[val - num]:
                dp[val] += dp[val - num]
    return dp[-1]


#nums = [2,20,24,38,44,21,45,48,30,48,14,9,21,10,46,46,12,48,12,38]
#S = 48
nums = [1, 1, 1, 1, 1]
S = 30000
print(findTargetSumWays(nums, S))