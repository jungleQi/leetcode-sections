def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices: return 0
    curmin = curmax = prices[0]
    maxProt = 0

    for price in prices:
        if price <= curmin:
            curmax = curmin = price
        elif price > curmax:
            curmax = price
        maxProt = max(maxProt, curmax - curmin)
    return maxProt
