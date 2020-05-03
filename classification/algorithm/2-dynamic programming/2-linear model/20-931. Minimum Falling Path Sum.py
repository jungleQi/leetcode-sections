#coding=utf-8

'''
Given a square 7-array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.
The next row's choice must be in a column that is different from the previous row's column by at most one.
'''

def minFallingPathSum_I(A):
    N = len(A)
    dp = [[0] * N for _ in range(N)]
    dp[0] = A[0]

    for i in range(1, N):
        for j in range(N):
            dp[i][j] = A[i][j]
            if j == 0:
                dp[i][j] += min(dp[i - 1][j], dp[i - 1][j + 1])
            elif j == N - 1:
                dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])
            else:
                dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])
    return min(dp[-1])

def minFallingPathSum_II(A):
    N = len(A)
    dp = [[0] * N for _ in range(N)]
    dp[0] = A[0]

    for i in range(1, N):
        for j in range(N):
            #这里的 max(0,j-1):min(j+2,N) 非常优雅的处理了边缘索引取值问题，不需要 I方案 那么多if分支
            items = dp[i-1][max(0,j-1):min(j+2,N)]
            dp[i][j] = A[i][j] + min(items)
    return min(dp[-1])

def minFallingPathSum_III(A):
    N = len(A)
    while len(A) >= 2:
        row = A.pop()
        for i in range(N):
            A[-1][i] += min(row[max(0,i-1):min(N,i+2)])
    return min(A[0])

A = [[17,82],[1,-44]]
print(minFallingPathSum_III(A))