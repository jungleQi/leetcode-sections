'''
Given n, how many structurally unique BST's (6-binary 7-search trees) that store values 1 ... n?
'''

def numTrees(n):
    dp = [1]*(n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1]*2
        for j in range(1,i-1):
            dp[i] += dp[j]*dp[i-1-j]
    return dp[-1]

print(numTrees(0))
