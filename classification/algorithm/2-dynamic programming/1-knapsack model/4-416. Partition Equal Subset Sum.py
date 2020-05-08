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
#dp[i]表示 和为j，是否存在
def canPartition(nums):
    target, res = divmod(sum(nums), 2)
    if res != 0: return False
    dp = [True] + [False] * target

    # 坑-1.循环嵌套顺序如果颠倒，就会出错
    # 这样可以确保一个Num只被使用一次，如果颠倒，就有可能一个Num被使用多次
    # 坑-2.第二层循环，不是从targe -> 1递减迭代 就会出错
    for num in nums:
        for i in range(target, 0, -1):
            if i >= num:
                dp[i] = dp[i] or dp[i - num]

    return dp[-1]

#dp[i][t] 前i个数中，是否有数字组成的和为t
def canPartition_2D(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    n = len(nums)

    dp = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        dp[i][0] = True

    for j in range(1, target + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= nums[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

    return dp[n][target]

nums = [1, 5, 11, 5]
print canPartition(nums)



