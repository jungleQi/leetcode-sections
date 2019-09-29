def coinChange(coins, amount):
    if amount == 0: return 0
    if not coins: return -1

    dp = [-1]*(amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        minCnt = i+1
        for coin in coins:
            if i>=coin and dp[i-coin] != -1 and dp[i-coin]+1 <= minCnt:
                minCnt = dp[i-coin]+1
        if minCnt <= i:
            dp[i] = minCnt
    return dp[-1]

coins =[1]
amount = 0
print coinChange(coins, amount)