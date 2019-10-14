def largestSumOfAverages(A, K):
    N = len(A)
    dp = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for j in range(1,K):
            m = i-1
            while m>=0:
                dp[i][j] = (dp[m][j-1]+sum(A[m:i+1])/(i+1-m), dp[i][j])
                m -= 1