def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    mid = 0
    N = len(nums)
    le, ri = 0, N - 1

    # get mid pos
    while le <= ri:
        mid = (le + ri) / 2
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            le = mid + 1
        else:
            ri = mid - 1

    if not nums or nums[mid] != target:
        return [-1, -1]

    # get first pos
    l, r = 0, mid
    while l < r:
        mid = (l + r) / 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    firstPos = l

    #get first pos
    l, r = mid, N - 1
    while l < r:
        mid = (l + r) / 2 + 1
        if nums[mid] <= target:
            l = mid
        else:
            r = mid - 1
    lastPos = l

    return [firstPos, lastPos]