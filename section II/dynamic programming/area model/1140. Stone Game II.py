def stoneGameII(piles):
    N = len(piles)
    for i in range(N-2, -1, -1):
        piles[i] += piles[i+1]

    hash = [[0 for _ in range(N)] for _ in range(N)]
    def dp(i,m):
        if i+2*m >= N: return piles[i]
        if hash[i][m]: return hash[i][m]
        hash[i][m] = piles[i]-min(dp(i+x,max(m,x)) for x in range(1, 2*m+1))
        return hash[i][m]
    return dp(0,1)

piles = [2,7,9,4,4]
print(stoneGameII(piles))