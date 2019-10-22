#coding=utf-8

#if S is very big，cause Memory Limit Exceeded
def test1(nums,S):
    total = sum(nums)
    if total < S: return 0

    target,mod = divmod(total+S, 2)
    if mod != 0: return 0

    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for num in nums:
        for j in range(target, num-1, -1):
            if dp[j-num]:
                dp[j] += dp[j-num]

    return dp[-1]

S = 3
nums = [1, 1, 1, 1, 1]
print test1(nums,S)