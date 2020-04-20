def minDistance(word1, word2):
    M, N = len(word1), len(word2)
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for i in range(1,M+1):
        for j in range(1,N+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return M+N-2*dp[-1][-1]

word1 = "s"
word2 = "e"
print(minDistance(word1, word2))