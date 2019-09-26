def longestPalindromeSubseq(s):
    N = len(s)
    dp = [[1 for _ in range(N)] for _ in range(N)]

    for i in range(1,N):
        for j in range(i-1, -1,-1):
            if s[j] == s[i]:
                if i-j>=2:
                    dp[j][i] = dp[j+1][i-1] + 2
                else:
                    dp[j][i] = 2
            else:
                dp[j][i] = max(dp[j+1][i],dp[j][i-1])

    return dp[0][-1]


s = "abdba"
print longestPalindromeSubseq(s)
