def findMaxForm(strs, m, n):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for str in strs:
        num_0, num_1 = str.count('0'), str.count('1')
        for i in range(m, num_0-1, -1):
            for j in range(n, num_1-1, -1):
                dp[i][j] = max(dp[i-num_0][j-num_1] + 1,dp[i][j])

    return dp[-1][-1]

#strs = {"10", "0", "1"}
#m,n = 1,1
strs = {"1100"}
m,n = 1,1
print(findMaxForm(strs, m, n))