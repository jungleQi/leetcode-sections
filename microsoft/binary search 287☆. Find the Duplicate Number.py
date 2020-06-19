def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    lo, hi = 0, N - 1

    while lo < hi:
        mid = (lo + hi) / 2

        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1

        if cnt <= mid:
            lo = mid + 1
        else:
            hi = mid
    return lo