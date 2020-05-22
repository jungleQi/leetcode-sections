def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxsum = cursum = nums[0]
    for num in nums[1:]:
        cursum = max(cursum + num, num)
        maxsum = max(maxsum, cursum)
    return maxsum