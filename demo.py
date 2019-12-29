def maxProfit(prices):
    maxsum, start, end = 0,0,0
    for i, p in enumerate(prices):
        if i>0 and p>=prices[i-1]:
            end = p
        else:
            maxsum += end-start
            start = end = p
    maxsum += end-start
    return maxsum

prices = [4,3,8]
print(maxProfit(prices))