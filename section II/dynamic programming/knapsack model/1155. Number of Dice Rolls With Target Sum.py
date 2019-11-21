'''
You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to roll the dice
so the sum of the face up numbers equals target.
'''

def numRollsToTarget(d, f, target):
    dp = [[0]*(target+1) for _ in range(d+1)]
    dp[0][0] = 1
    for i in range(1, d+1):
        for j in range(i,target+1):
            for m in range(1,f+1):
                if m<=j:
                    dp[i][j] += dp[i-1][j-m]

    return dp[-1][-1]%(10**9+7)
d = 2
f = 6
target = 7
print(numRollsToTarget(d, f, target))
