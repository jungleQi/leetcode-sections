def findDisappearedNumbers(nums):
    res = []
    for num in nums:
        if num == 0: continue

        curidx = num-1
        while nums[curidx] != 0:
            tmp = nums[curidx]-1
            nums[curidx] = 0
            curidx = tmp

    for idx, num in enumerate(nums):
        if num != 0:
            res.append(idx+1)

    return res

nums = [4,3,2,7,7,2,3,1]
print findDisappearedNumbers(nums)