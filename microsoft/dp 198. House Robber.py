def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    prevMax = curMax = 0
    for num in nums:
        prevMax, curMax = curMax, max(prevMax + num, curMax)
    return max(prevMax, curMax)