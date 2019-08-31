def numTrees(n):
    if n == 0:
        return 0
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(1,n+1):
        for j in range(1,i-1):
            dp[i] += dp[j]*dp[i-j-1]
        dp[i] += dp[i-1]*2
    return dp[-1]

print(numTrees(3))