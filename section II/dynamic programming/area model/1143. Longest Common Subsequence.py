#coding=utf-8

def longestCommonSubsequence(text1, text2):
    N = len(text1)
    M = len(text2)
    if N == 0 or M == 0:
        return 0

    dp = [[0 for _ in range(M)] for _ in range(N)]
    #frontier
    dp[0][0] = 1 if text1[0] == text2[0] else 0
    #recursive
    for i in range(N):
        for j in range(M):
            if i == 0:
                dp[i][j] = 1 if text1[0] in text2[:j+1] else 0
                continue
            if j == 0:
                dp[i][j] = 1 if text2[0] in text1[:i+1] else 0
                continue

            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]

text1 ="abc"
text2 = "def"
print longestCommonSubsequence(text1, text2)
