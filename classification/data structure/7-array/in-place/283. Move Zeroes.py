def moveZeroes(nums):
    newBack = -1
    for idx, num in enumerate(nums):
        if num == 0: continue
        newBack += 1
        nums[newBack] = num
        if newBack != idx:
            nums[idx] = 0

nums =[0,1]
moveZeroes(nums)
print(nums)