def maxSubArray(nums):
    cursum, maxsum = 0, nums[0]
    for num in nums:
        cursum += num
        maxsum = max(maxsum, cursum)

        if cursum < 0:
            if num<0:
                cursum = 0
            else:
                cursum = num

    return maxsum

nums = [-1,0]
print(maxSubArray(nums))

