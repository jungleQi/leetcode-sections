def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    if N == 1: return nums[0]
    if nums[-1] <= nums[-2]: return nums[-1]

    lo, hi = 0, N - 1
    while lo < hi:
        if nums[lo] < nums[hi]:
            return nums[lo]

        mid = (lo + hi) / 2
        if nums[lo] < nums[mid]:
            lo = mid + 1
        elif nums[lo] > nums[mid]:
            hi = mid
        else:
            return min(nums[lo], nums[hi])
    return nums[lo]