import sys
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