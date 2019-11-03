def maxProfit(prices):
    if not prices: return 0

    maxprofit,minval = 0, prices[0]
    for price in prices:
        if price < minval:
            minval = price
            continue
        maxprofit = max(maxprofit, price-minval)

    return maxprofit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))