'''
Given an 2-array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1,
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
'''

import collections

def longestArithSeqLength(A):
    N = len(A)
    dp = [[2]*N for _ in range(N)]
    m = {}
    for i in range(N):
        for j in range(i+1, N):
            v = A[i]-(A[j]-A[i])
            if v in m:
                dp[i][j] = dp[m[v]][i]+1
        m[A[i]] = i
    #print(dp)
    return max(max(row) for row in dp)


A = [100,0,1,100,0,94,3,0,3]
print(longestArithSeqLength(A))