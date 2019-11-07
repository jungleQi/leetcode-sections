'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''

#[7,1,5,3,6,4]
def maxProfit(prices):
    if not prices: return 0

    minVal, maxprofit = prices[0], 0
    for price in prices:
        if price < minVal:
            minVal = price
            continue
        maxprofit = max(maxprofit, price - minVal)

    return maxprofit
prices = [7,6,4,3,1]
print(maxProfit(prices))