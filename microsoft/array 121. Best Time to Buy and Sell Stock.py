def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    ans = 0
    minPrice = float("inf")
    for price in prices:
        if price <= minPrice:
            minPrice = price
        else:
            ans = max(ans, price - minPrice)
    return ans