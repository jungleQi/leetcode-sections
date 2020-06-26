#coding=utf-8

'''
Say you have an 2-array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
'''

'''
dp[k][i] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions.
state transition equation:
    dp[k][i] = max(dp[k][i-1], max(dp[k-1][j]+prices[i]-prices[j]) j->[1:j] ==> 3 level loop will cause tle
    
    evolution:
    dp[k][i] = max(dp[k][i-1], prices[i] + max(dp[k-1][j]-prices[j])) j->[1:j] => 2 level loop
'''

def maxProfit(k, prices):
    N = len(prices)
    if N==0 or k==0: return 0

    #当k>N/2，就能把每次价格上涨的收益都拿到
    if k>N/2:
        profit = 0
        for i in range(1,N):
            diff = prices[i]-prices[i-1]
            if diff > 0: profit += diff
        return profit

    dp = [[0]*N for _ in range(k)]
    for i in range(k):
        maxprofit = -prices[0]
        for j in range(1,N):
            maxprofit = max(maxprofit, dp[i-1][j]-prices[j])
            dp[i][j] = max(dp[i][j-1], maxprofit + prices[j])

    return dp[-1][-1]

k = 2
prices = [2]
print(maxProfit(k, prices))