import math

def numSquares(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2,n+1):
        minVal = i
        sqrtCnt = int(math.sqrt(i))+1
        for j in range(1, sqrtCnt+1):
            if i-j*j >= 0 and dp[i-j*j]<minVal:
                minVal = dp[i-j*j]
        dp[i] = minVal+1

    return dp[-1]

n = 13
print(numSquares(n))



