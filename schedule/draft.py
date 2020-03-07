def combinationSum3(k, n):
    def helper(nums, k, n, path, ret):
        if k == 0 and n == 0:
            ret.append(path)
            return

        for i, num in enumerate(nums):
            if num > n: return
            helper(nums[i+1:], k-1, n-num, path+[num], ret)

    nums = range(1,10)
    ans = []
    helper(nums, k, n, [], ans)
    return ans

k,n = 0,0
print(combinationSum3(k, n))