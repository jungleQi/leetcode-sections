#coding=utf-8

#dp[target]有多少种可能，就需要一次遍历nums，看每个num在选择和不选择两种情况下的累积数量
#选择，那就是dp[target-num]中可能；不选择，就是dp[target];所以,在遍历过程中，有一个积累：
#dp[target] = dp[target] + dp[target-num]

#为了求得dp[target-num],就需要bottem up的方式，循环依次求dp[1..target]的每一级累积值，为自后的dp[target]奠定基础
#因为是要求的dp[i]的最大数，所以，内层循环遍历需要对每个nums进行一个判断，将dp[target]循环放在外层
def combinationSum4(nums, target):
    dp = [1]+[0]*target

    for i in range(target + 1):
        for n in nums:
            if n<=i:
                dp[i] += dp[i-n]

    return dp[-1]

nums = [1, 2, 3]
target = 4
print combinationSum4(nums, target)