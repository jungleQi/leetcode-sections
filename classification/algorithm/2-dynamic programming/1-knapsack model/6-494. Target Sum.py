#coding=utf-8
import sys

'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
'''

#TAG: 2D->1D：双层遍历顺序不可颠倒，单层遍历target递减遍历；
def findTargetSumWays_2d_knapsack(nums,S):
    #if S is very big，causing Memory Limit Exceeded
    total = sum(nums)
    if total < S: return 0

    #target - s2 = S, target + s2 = sum(nums)
    # --> target = (sum(nums)+S)/2
    #将问题转换成背包问题，从nums中挑选数字序列，每组序列的和为target，这样的组合有多少种
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

import math
def findTargetSumWays(nums, S):
    s = sum(nums)
    if (s + S) % 2 != 0 or s < math.fabs(S): return 0

    dst = (s + S) / 2
    dp = [1] + [0] * dst
    for num in nums:
        for i in range(dst, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[-1]

nums = [1, 1, 1, 1, 1]
S = 3
print(findTargetSumWays(nums, S))