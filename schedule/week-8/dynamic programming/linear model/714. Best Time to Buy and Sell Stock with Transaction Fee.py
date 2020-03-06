'''
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i;
and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.
'''

def maxProfit(prices, fee):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
        cash = max(cash, hold+prices[i]-fee)
        hold = max(hold, cash-prices[i])
    return max(cash, hold)

prices = [3,3,5,3,2,1,4,2,5,3]
fee = 1
print(maxProfit(prices, fee))
