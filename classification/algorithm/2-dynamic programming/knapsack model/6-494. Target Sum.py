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

def findTargetSumWays(nums, S):
    s = sum(nums)
    if s <S: return 0

    target,mod = divmod(s+S,2)
    if mod != 0: return 0

    dp = [0]*(target+1)
    dp[0] = 1
    # 嵌套loop的顺序颠倒了，每次累积的数目，会用到后面(全局)的累积数，导致数目倍数增长而偏大
    for n in nums:
        # 该层遍历的顺序如果不倒序，就会导致同一个数字，每个t都会复用t-1的累积数导致结果偏大
        for t in range(target, n-1, -1):
            #避免t-n是负数，或者说t-n是合理的索引，只需设定range(target, n-1, -1)，既可以让t在合理范围内，有可以减少遍历次数
            dp[t] += dp[t-n]

    return dp[-1]

nums = [1, 1, 1, 1, 1]
S = 3
print(findTargetSumWays(nums, S))