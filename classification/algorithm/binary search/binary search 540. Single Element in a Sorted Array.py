def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    l, h = 0, N - 1

    while l < h:
        mid = (h + l) / 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            l = mid + 2
        else:
            h = mid
    return nums[l]