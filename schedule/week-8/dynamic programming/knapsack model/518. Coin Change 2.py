def change_2D(amount, coins):

    N = len(coins)
    dp = [[0 for _ in range(amount+1)] for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(amount+1):
            if coins[i-1] <= j:
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

def change(amount, coins):
    dp = [1]+[0]*amount

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i-coin]

    return dp[-1]

amount = 5
coins = [1,2,5]
print(change(amount, coins))