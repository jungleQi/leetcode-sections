'''
We partition a row of numbers A into at most K adjacent (non-empty) groups,
then our score is the sum of the average of each group.
What is the largest score we can achieve?

Note that our partition must use every number in A,
and that scores are not necessarily integers.
'''

#[9,1,2,3,9]
import collections
def largestSumOfAverages(A, K):
    N   = len(A)
    dp  = [[0]*(K+1) for _ in range(N+1)]

    for k in range(1,K+1):
        for m in range(k, N+1):
            if k == 1:
                dp[m][k] = sum(A[:m])*1.0/m
                continue
            for j in range(k,m+1):
                dp[m][k] = max(dp[m][k], dp[j-1][k-1] + sum(A[j-1:m])*1.0/(m-j+1))

    return dp[-1][-1]


def largestSumOfAverages_online(A, K):
    N = len(A)

    def avg(i,j):
        return sum(A[i:j+1])*1.0/(j+1-i)

    dp = [avg(i,N-1) for i in range(N)]
    for k in range(1,K):
        for i in range(N-k):
            for j in range(i+1, N):
                dp[i] = max(dp[i], avg(i,j-1) + dp[j])
    return dp[0]

A = [9,1,2,3,9]
K = 3
print(largestSumOfAverages_online(A, K))
