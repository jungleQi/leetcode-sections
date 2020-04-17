#coding=utf-8
from utils import Node
import heapq
import collections


def findMaxForm(strs, m, n):
    dp = [[0]*(n+1) for _ in range(m+1)]
    for str in strs:
        n0, n1 = str.count('0'), str.count('1')
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if n0 > i or n1>j: break
                dp[i][j] = max(dp[i][j], dp[i-n0][j-n1]+1)
    return dp[-1][-1]

strs = {"10", "0001", "111001", "1", "0"}
m = 0
n = 0
print findMaxForm(strs, m, n)
