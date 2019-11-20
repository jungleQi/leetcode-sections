'''

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers.
Return the maximum product you can get.

'''

def integerBreak(n):
    dp = [i-1 for i in range(n+1)]

    for i in range(2,n+1):
        for j in range(1,i):
            dp[i] = max(dp[i], dp[j]*dp[i-j], j*(i-j), dp[j]*(i-j))
    return dp[-1]

print(integerBreak(2))
