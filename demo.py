#coding=utf-8
import sys

def findTargetSumWays(nums, S):
    s = sum(nums)
    if s <S: return 0
    target,mod = divmod(s+S,2)
    if mod != 0: return 0

    dp = [0]*(target+1)
    dp[0] = 1
    for n in nums:#嵌套loop的顺序颠倒了，每次累积的数目，会用到后面(全局)的累积数，导致数目倍数增长而偏大
        for t in range(target, n-1, -1): #该层遍历的顺序如果不倒序，就会导致同一个数字，每个t都会复用t-1的累积数导致结果偏大
            #避免t-n是负数，或者说t-n是合理的索引，只需设定range(target, n-1, -1)，既可以让t在合理范围内，有可以减少遍历次数
            if dp[t-n]:
                dp[t] += dp[t-n]

    return dp[-1]

nums = [1, 1, 1, 1, 1]
S = 3
print(findTargetSumWays(nums, S))