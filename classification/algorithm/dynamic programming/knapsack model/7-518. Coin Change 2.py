#coding=utf-8

'''
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
'''

def change_2D(amount, coins):

    N = len(coins)
    dp = [[0 for _ in range(amount+1)] for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(amount+1):
            dp[i][j] = dp[i - 1][j]
            if coins[i-1] <= j:
                dp[i][j] += dp[i][j-coins[i-1]]

    return dp[-1][-1]

def change(amount, coins):
    dp = [1]+[0]*amount

    for coin in coins:
        #一个coin可以选择多次，所以下面采用coin -> amount+1的升序遍历
        #如果一个coin只能选择一次，就需要采用amount+1 ->coin的降序
        for i in range(coin, amount + 1):
            dp[i] += dp[i-coin]

    return dp[-1]

amount = 5
coins = [1,2,5]
print(change(amount, coins))