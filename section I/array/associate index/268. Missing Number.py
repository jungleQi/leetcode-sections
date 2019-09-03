def missingNumber(nums):
    cnt = len(nums)
    for num in nums:
        while num<cnt and num>=0 and nums[num] >= 0:
            nums[num], num = -1, nums[num]

    for idx, num in enumerate(nums):
        if num != -1:
            return idx

    return cnt

nums = []
print missingNumber(nums)