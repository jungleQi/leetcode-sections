def permuteUnique(nums):
    def dfs(nums, result, results):
        if not nums:
            results += result,
            return

        prevNum = nums[0]
        for idx, num in enumerate(nums):
            if idx >0 and num == prevNum:
                continue

            prevNum = num
            dfs(nums[:idx]+nums[idx+1:], result+[num], results)

    results = []
    nums.sort()
    dfs(nums, [], results)
    return results

nums = [1,1,]
ret = permuteUnique(nums)
print(ret)