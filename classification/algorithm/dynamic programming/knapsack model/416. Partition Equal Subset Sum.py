#coding=utf-8

def canPartition_dfs(nums):
    sumer = sum(nums)
    if sumer & 1 == 1:
        return False
    nums.sort(reverse=True)

    def dfs(index, target):
        if target == 0:
            return True
        if index == len(nums) or target < nums[index]:
            return False

        return dfs(index+1, target-nums[index]) or dfs(index+1, target)

    return dfs(0, sumer//2)

#knapsack 0/1
#dp[i][j]表示 前i件物品的和为j，是否存在
def canPartition(nums):
    target, res = divmod(sum(nums), 2)
    if res != 0: return False

    N = len(nums)
    dp = [False for _ in range(target + 1)]
    dp[0] = True
    for i in range(1, N + 1):
        for j in range(target, 0, -1):
            if j == nums[i - 1]:
                dp[j] = True
            elif j > nums[i - 1]:
                dp[j] = dp[j] or dp[j - nums[i - 1]]

    return dp[-1]

nums = [1, 5, 11, 5]
print canPartition(nums)



