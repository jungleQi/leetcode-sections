def removeDuplicates(nums):
    newBack = -1
    repeatCnt = 1
    for num in nums:
        if newBack >=0 and num == nums[newBack]:
            if repeatCnt >= 2:
                continue
            repeatCnt += 1
        else:
            repeatCnt = 1

        newBack += 1
        nums[newBack] = num

    return newBack+1

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums), nums)
