def maximalSquare(matrix):
    M = len(matrix)
    if M == 0: return 0
    N = len(matrix[0])

    maxSidelen = 0
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for i in range(1, M+1):
        for j in range(1, N+1):
            if matrix[i-1][j-1] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                maxSidelen = max(maxSidelen, dp[i][j])

    return maxSidelen*maxSidelen

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(matrix))