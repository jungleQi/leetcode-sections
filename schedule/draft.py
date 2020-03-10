def subsetsWithDup(nums):
    def helper(nums, set, ret):
        for i, num in enumerate(nums):
            if i>0 and nums[i-1] == num: continue
            ret.append(set+[num])
            helper(nums[i+1:], set+[num], ret)

    nums.sort()
    ret = [[]]
    helper(nums, [], ret)
    return ret

nums = [1,2,2]
print(subsetsWithDup(nums))