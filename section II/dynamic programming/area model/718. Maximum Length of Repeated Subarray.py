def findLength(A, B):
    M, N = len(A), len(B)
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

    maxlen = 0
    for i in range(1,M+1):
        for j in range(1,N+1):
            if A[i-1] == B[j-1]:
                dp[i][j] =  dp[i-1][j-1] + 1
                maxlen = max(maxlen, dp[i][j])

    #print(dp)
    return maxlen

A = [0,1,1,1,1]
B = [1,0,1,0,1]
print(findLength(A, B))