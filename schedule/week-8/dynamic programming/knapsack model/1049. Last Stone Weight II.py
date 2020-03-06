def lastStoneWeightII(stones):
    dp = {0}
    allsum = sum(stones)

    for weight in stones:
        dp |= {weight+i for i in dp}

    return min(abs(allsum-i-i) for i in dp)

stones = [2,7]
print lastStoneWeightII(stones)