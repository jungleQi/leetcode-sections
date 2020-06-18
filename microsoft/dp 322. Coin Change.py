def coinChange(coins, amount):
    dp = [0] + [float("inf")] * amount

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i - coin] + 1, dp[i])
    return dp[-1] if dp[-1] != float("inf") else -1