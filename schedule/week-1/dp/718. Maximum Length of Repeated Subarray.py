'''
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
'''

def findLength(A, B):
    N,M = len(A),len(B)
    dp = [[0]*(M+1) for _ in range(N+1)]

    i,maxlen = 1,0
    while i<=N:
        j = 1
        while j<=M:
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                maxlen = max(maxlen, dp[i][j])
            j += 1
        i += 1
    return maxlen

A = [10]
B = [10]
print(findLength(A, B))
