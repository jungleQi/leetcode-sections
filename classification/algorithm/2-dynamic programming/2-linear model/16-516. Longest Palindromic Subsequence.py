#coding=utf-8

'''
Given a 5-string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.
'''

def longestPalindromeSubseq_ErrorTrap(s):
    N = len(s)
    if N == 0: return 0

    dp = [[1] * N for _ in range(N)]
    for i in range(1, N):
        #ERROR: [0, ... i-1] 的遍历，逻辑上是有问题的，应该是[i-1 ,..., 0]
        for j in range(i):
            if s[j] == s[i]:
                if i - j > 1:
                    #这里没有必要这么复杂，dp[j][i] = dp[j + 1][i - 1] + 2 就可以了
                    dp[j][i] = max(dp[j + 1][i - 1] + 2, dp[j][i - 1], dp[j + 1][i])
                else:
                    dp[j][i] = 2
            else:
                if i - j > 1:
                    dp[j][i] = max(dp[j][i - 1], dp[j + 1][i])
    return dp[0][-1]


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