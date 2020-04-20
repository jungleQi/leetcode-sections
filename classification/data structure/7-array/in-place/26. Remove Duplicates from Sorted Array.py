def removeDuplicates(nums):
    newBack, curIdx = 0,1
    cnt = len(nums)
    while curIdx<cnt:
        if nums[newBack] != nums[curIdx]:
            newBack += 1
            nums[newBack] = nums[curIdx]
        curIdx += 1

    return newBack+1

nums = [1,1]
print(removeDuplicates(nums))