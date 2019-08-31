def removeElement(nums, val):
    newBack = -1
    for num in nums:
        if num == val:continue
        newBack += 1
        nums[newBack] = num
    return newBack+1

nums = [1,1,1,2,1,2,1,1]
val =1
print(removeElement(nums, val))