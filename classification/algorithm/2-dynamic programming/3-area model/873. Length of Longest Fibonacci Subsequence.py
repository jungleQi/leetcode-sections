'''
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing 2-array A of positive integers forming a sequence,
find the length of the longest fibonacci-like subsequence of A.
If one does not exist, return 0.

'''

import collections

def lenLongestFibSubseq(A):
    N = len(A)
    dp = [[2] * (N + 1) for _ in range(N + 1)]
    numdict = collections.defaultdict(lambda: N + 2)
    for idx, n in enumerate(A):
        numdict[n] = idx + 1

    ans = 0
    for i in range(1, N + 1):
        for j in range(i - 1, 1, -1):
            idx = numdict[A[i - 1] - A[j - 1]]
            if idx < j:
                dp[j][i] = dp[idx][j] + 1
                ans = max(ans, dp[j][i])
    return ans

def lenLongestFibSubseq_fast(A):
    index = {x:i for i,x in enumerate(A)}
    longest = collections.defaultdict(lambda :2)

    ans = 0
    for i,n in enumerate(A):
        for j in range(i-1,0,-1):
            k = index.get(A[i]-A[j], None)
            if k is not None and k<j:
                longest[j,i] = longest[k,j]+1
                ans = max(ans, longest[j,i])
    return ans

A = [1,2,3]
print(lenLongestFibSubseq_fast(A))
