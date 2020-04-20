'''
Given a 6-string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.
'''

def longestPalindromeSubseq(s):
# dp[i] is, item[i] as start-point, can construct the current largest substr
    N = len(s)
    if s == s[::-1]: return N

    dp = [0]*N
    dp[0] = 1
    for i in range(1,N):
        former_dp = dp[:]

        for j in range(i-1,-1,-1):
            if s[j] == s[i]:
                dp[j] = former_dp[j+1]+2
            else:
                dp[j] = max(former_dp[j],dp[j+1])
        dp[i] = 1
    return dp[0]

s = "ba"
print(longestPalindromeSubseq(s))