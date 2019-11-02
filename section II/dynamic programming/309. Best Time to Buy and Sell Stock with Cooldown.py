def maxProfit(prices):
    N = len(prices)
    dp = [0]*(N+1)
    for i in range(2,N+1):
        for j in range(1,i):
            if prices[j]<prices[i]:
                dp[i] = max(dp[i], dp[j-2])
