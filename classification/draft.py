#coding=utf-8
from utils import Node
import heapq
import collections

def change(amount, coins):
    N = len(coins)
    dp = [[0] * (N + 1) for _ in range(amount + 1)]
    dp[0][0] = 1

    for i in range(amount + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= coins[j - 1]:
                dp[i][j] += dp[i - coins[j - 1]][j]
    return dp[-1][-1]

coins = [1,2,5]
amount = 5
print change(amount, coins)