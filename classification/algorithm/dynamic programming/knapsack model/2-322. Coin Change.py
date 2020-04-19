#coding=utf-8
import sys

'''
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
'''

def coinChange_2D(coins, amount):
    if amount == 0: return 0

    N = len(coins)
    dp = [[sys.maxint for _ in range(amount + 1)] for _ in range(N + 1)]

    dp[0][0] = 0
    for j in range(1, amount + 1):
        for i in range(1, N + 1):
            if coins[i - 1] == j:
                dp[i][j] = 1
            elif coins[i - 1] < j:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

    return -1 if dp[-1][-1] == sys.maxint else dp[-1][-1]


def coinChange_1D(coins, amount):
    if amount == 0: return 0

    dp = [sys.maxint]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin<=i:
                dp[i] = min(dp[i], dp[i-coin]+1)

    return dp[i] if dp[i] != sys.maxint else -1

coins =[186,419,83,408]
amount = 6249
print coinChange_1D(coins, amount)