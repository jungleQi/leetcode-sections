def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hist = {}
    for i, num in enumerate(nums):
        j = hist.get(target - num, -1)
        if j >= 0:
            return [j, i]
        hist[num] = i