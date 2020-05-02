#coding=utf-8

'''
Alex and Lee continue their games with piles of stones.  There are a number of piles arranged in a row,
and each pile has a positive integer number of stones piles[i].  The objective of the 6-game is to end with the most stones.

Alex and Lee take turns, with Alex starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.
Then, we set M = max(M, X).

The 6-game continues until all the stones have been taken.

Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.
'''

'''
函数f(i,M)，表示在piles[i:]中以[1,2*M]为取值范围可以取的最多石子数

f(i,M)=sum(piles[i:])−min(f(i+x,max(M,x)))  (1≤x≤2∗M)
也就是说，我们希望亚历克斯尽可能多拿的话，那么我们就希望李少拿。亚历克斯最多拿sum(piles[i:])个石子，
而李最少拿min(f(i+x,max(M, x)))个石子，最后亚历克斯实际上可以最多拿二者之差个石子

'''

def stoneGameII(piles):
    N = len(piles)
    for i in range(N - 2, -1, -1):
        piles[i] += piles[i + 1]

    hash = [[0 for _ in range(N)] for _ in range(N)]

    def dp(i, m):
        if i + 2 * m >= N: return piles[i]
        if hash[i][m]: return hash[i][m]
        hash[i][m] = piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return hash[i][m]

    return dp(0, 1)

piles = [2,7,9,4,4]
print(stoneGameII(piles))