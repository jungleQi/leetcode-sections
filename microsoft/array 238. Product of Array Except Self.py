def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    N = len(nums)
    ret = [1] * N

    for i in range(1, N):
        ret[i] = ret[i - 1] * nums[i - 1]

    right = 1
    for i in range(N - 1, -1, -1):
        ret[i] = ret[i] * right
        right = right * nums[i]
    return ret