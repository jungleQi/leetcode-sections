def largestSumOfAverages(A, K):
    N = len(A)
    if K>=N: return sum(A)*1.0

    dp = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for k in range(min(i+1,K)):
            if k == 0:
                dp[i][k] = sum(A[:i + 1])/(i+1)
                continue

            m = i-1
            while m>=0:
                dp[i][k] = max(dp[m][k-1]+sum(A[m+1:i + 1])/(i-m), dp[i][k])
                m -= 1
    #print(dp)
    return dp[-1][-1]

A = [9,1,2,3,9]
K = 3
#A = [9,3,1,5]
#K = 2
print(largestSumOfAverages(A, K))