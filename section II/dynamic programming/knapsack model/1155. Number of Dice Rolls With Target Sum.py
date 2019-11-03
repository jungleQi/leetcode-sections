def numRollsToTarget(d, f, target):
    dp = [[0 for _ in range(target+1)] for _ in range(d+1)]
    dp[0][0] = 1

    for i in range(1,d+1):
        for j in range(1,target+1):
            for m in range(1,f+1):
                if m<=j:
                    dp[i][j] = dp[i][j] + dp[i-1][j-m]

    return dp[-1][-1]

d = 1
f = 2
target = 3
print(numRollsToTarget(d, f, target))