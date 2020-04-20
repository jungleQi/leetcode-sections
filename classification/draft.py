#coding=utf-8
from utils import Node
import heapq
import collections

def numRollsToTarget(d, f, target):
    dp = [1]+[0]*target

    for i in range(1, d + 1):
        for j in range(target, 0, -1):
            for k in range(1, f + 1):
                if k > j: break
                dp[j] += dp[j-k]
    return dp[-1] % (10**9 + 7)

d = 30
f = 30
target = 500
print numRollsToTarget(d, f, target)