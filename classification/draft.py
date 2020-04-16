#coding=utf-8
from utils import Node
import heapq
import collections

def canPartition(nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            dp[i][0] = True

        for j in range(1, target + 1):
            dp[0][j] = False

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[n][target]

nums = [1,2,5]
print canPartition(nums)

