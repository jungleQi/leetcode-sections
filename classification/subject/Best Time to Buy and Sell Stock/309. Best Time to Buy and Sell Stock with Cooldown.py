#coding=utf-8

'''
Say you have an 2-array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times)
with the following restrictions:

You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day.
(ie, cooldown 1 day)

'''

'''
高效的状态，一层循环：
hold[i] 第i天，持有股票时，获得的最大收益，
cash[i] 第i天，持有现金时，获得的最大收益，

低效的状态，两层嵌套循环：
buy[i] 第i天，买入股票时，获得的最大收益，
sell[i] 第i天，卖出股票时，获得的最大收益,

'''

#[1,2,3,0,2]
def maxProfit_unefficient(prices):
    N = len(prices)
    if N == 0: return 0

    buy = [0] * N
    sell = [0] * N
    for i in range(N):
        buy[i] = -prices[i]
        for j in range(i):
            if j < i - 1:
                buy[i] = max(buy[i], sell[j] - prices[i])
            sell[i] = max(sell[i], buy[j] + prices[i])

    return max(max(sell), max(buy))

def maxProfit(prices):
    N = len(prices)
    if N == 0: return 0

    hold = [0]*N
    cash = [0]*N

    hold[0] = -prices[0]
    for i in range(1,N):
        cash[i] = max(hold[i-1]+prices[i], cash[i-1])
        hold[i] = max(hold[i-1], (cash[i-2] if i>1 else 0)-prices[i])

    return cash[-1]


prices = [1,2,3,0,2]
print(maxProfit(prices))