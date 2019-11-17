'''
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
'''

#s1 = "delete", s2 = "leet"

def minimumDeleteSum(s1, s2):
    M,N = len(s1),len(s2)
    dp = [[0]*(N+1) for i in range(M+1)]

    for i in range(M+1):
        for j in range(N+1):
            if i ==0 and j == 0: continue

            if i == 0:
                dp[0][j] = dp[0][j-1] + ord(s2[j-1])
                continue

            if j == 0:
                dp[i][0] = dp[i-1][0] + ord(s1[i-1])
                continue

            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]))
    return dp[-1][-1]

s1 = "s"
s2 = "e"
print(minimumDeleteSum(s1, s2))