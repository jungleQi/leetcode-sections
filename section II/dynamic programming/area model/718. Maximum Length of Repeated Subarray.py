'''
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
'''

def findLength(A, B):
    maxlen = 0
    M, N = len(A), len(B)
    dp = [[0]*(N+1) for _ in range(M+1)]
    for i in range(1,M+1):
        for j in range(1,N+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                maxlen = max(maxlen, dp[i][j])
    return maxlen

A = [1]
B = [2]
print(findLength(A,B))