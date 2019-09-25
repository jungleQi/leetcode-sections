def test1(nums):
    if nums <= 2:
        return nums

    dp = [0]*(nums + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, nums + 1):
        ratio_cnt = int(math.sqrt(i)) + 1
        mincnt = i
        for ratio in range(1, ratio_cnt + 1):
            if i - ratio * ratio >= 0 and dp[i - ratio * ratio] < mincnt:
                mincnt = dp[i - ratio * ratio]
        dp[i] = mincnt + 1

    return dp[-1]