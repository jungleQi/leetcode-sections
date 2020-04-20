#coding=utf-8

'''
Given an integer 7-array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.
'''

#采用backtracking 会 TLE，采用DP 可 PASS

def combinationSum4_TLE(nums, target):
    def _helper(tar, ret):
        if tar < 0: return
        if tar == 0:
            ret[0] += 1
            return

        for n in nums:
            _helper(tar-n, ret)

    ret = [0]
    _helper(target,ret)
    return ret[0]

def combinationSum4(nums, target):
    dp = [1] +[0]*target
    for t in range(1,target+1):
        for n in nums:
            if n<=t: dp[t] += dp[t-n]

    return dp[-1]

nums = [4,2,1]
target = 32
print(combinationSum4(nums, target))