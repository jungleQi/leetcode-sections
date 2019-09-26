def countBits(num):
    dp = [0]*(num+1)
    for n in range(1,num+1):
        dp[n] = dp[n>>1] + n%2

    return dp

print(countBits(4))