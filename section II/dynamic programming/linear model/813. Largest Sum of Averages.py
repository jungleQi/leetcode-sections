def largestSumOfAverages(A, K):
    S = [0]
    N = len(A)
    for v in A: S.append(S[-1]+v)

    def average(i,j):
        return (S[j]-S[i])/float(j-i)

    dp = [average(i,N) for i in range(N)]
    for k in range(K-1):
        for i in range(N):
            for j in range(i+1, N):
                dp[i] = max(dp[i], average(i,j)+dp[j])
    return dp[0]

A = [9,1,2,3,9]
K = 3
#A = [9,3,1,5]
#K = 2
print(largestSumOfAverages(A, K))