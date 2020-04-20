def test(nums, target):
    def findNums(l, r, N, nums, target, result, results):
        if r-l+1<N or N<2 or nums[l]*N>target or nums[r]*N<target:
            return

        if N == 2:
            while l<r:
                if nums[l]+nums[r] < target:
                    l += 1
                elif nums[l]+nums[r] > target:
                    r -= 1
                else:
                    results += result+[nums[l], nums[r]],
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        else:
            for i in range(l, r):
                if i>l and nums[i] == nums[i-1]:
                    continue
                findNums(i+1, r, N-1, nums, target-nums[i], result+[nums[i]], results)

    results = []
    N = len(nums)
    nums.sort()

    findNums(0, N-1, 4, nums, target, [], results)
    return results

nums = [-1,-1,0,0]
target = -2
ret = test(nums, target)
print("ret:", ret)


























