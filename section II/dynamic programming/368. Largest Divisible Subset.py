def largestDivisibleSubset(nums):
    if not nums: return []
    dp = [[num] for num in nums]
    max_len, res = 1, dp[0]
    nums = sorted(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]%nums[j] == 0 and max_len <= len(dp[j])+1:
                dp[i] = dp[j]+[nums[i]]
                max_len,res = len(dp[i]), dp[i]

    return res

nums = [2,3,8,9,27]
print(largestDivisibleSubset(nums))

#submissions里面，有一个通过的解决方案，想了了很久没能理解，觉得有缺陷，后来找出了一组测试数据:[2,4,8,9,72,144]
#证实该方案确实是有问题的：
'''
        if not nums: return []

        dp = [[num] for num in nums]
        max_len, res = 1, dp[0]
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0:
                    dp[i] = dp[j]+[nums[i]]  #this is fault! 
                    if max_len < len(dp[i]):
                        max_len,res = len(dp[i]), dp[i]

        return res
'''
