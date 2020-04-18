#coding=utf-8
from utils import Node
import heapq
import collections

def findTargetSumWays_2D(nums, S):
    numSum = sum(nums)
    if numSum < S: return 0

    target, mod = divmod(numSum+S, 2)
    if mod: return 0

    N = len(nums)
    dp = [[0]*(target+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(target+1):
            if nums[i-1]<=j:
                dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]

def findTargetSumWays_1D(nums, S):
    numSum = sum(nums)
    if numSum < S: return 0

    target, mod = divmod(numSum+S, 2)
    if mod: return 0

    N = len(nums)
    dp = [1] + [0]*target

    for i in range(1, N+1):
        for j in range(target, nums[i-1]-1, -1):
            dp[j] += dp[j-nums[i-1]]
    return dp[-1]

nums = [1, 1, 1, 1, 1]
S = 3
print findTargetSumWays_1D(nums, S)