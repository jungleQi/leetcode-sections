def longestPalindromeSubseq(s):
    """
    :type s: str
    :rtype: int
    """
    N = len(s)
    if s == s[::-1]:
        return N

    dp = [[1] * N for _ in range(N)]
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if s[i] == s[j]:
                if i != j + 1:
                    dp[j][i] = dp[j + 1][i - 1] + 2
                else:
                    dp[j][i] = 2
            else:
                dp[j][i] = max(dp[j][i - 1], dp[j + 1][i])
    return dp[0][-1]