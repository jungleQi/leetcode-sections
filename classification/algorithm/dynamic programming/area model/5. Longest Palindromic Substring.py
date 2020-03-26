def longestPalindrome(s):
    N = len(s)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    maxstr = s[0]
    for i in range(N):
        for j in range(i-1, -1, -1):
            dp[j][i] = (s[j] == s[i]) and (i-j<3 or dp[j+1][i-1])
            if dp[j][i] and i-j+1>len(maxstr):
                maxstr = s[j:i+1]

    return maxstr

s = "bbb"
print(longestPalindrome(s))