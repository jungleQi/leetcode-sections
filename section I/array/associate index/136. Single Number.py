def singleNumber(nums):
    a = 0
    for num in nums:
        a ^= num

    return a

nums = [2,1,1]
print singleNumber(nums)