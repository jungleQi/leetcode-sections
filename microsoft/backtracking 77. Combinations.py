def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """

    def helper(nums, path, k, ret):
        if k == 0:
            ret.append(path)
            return

        for i, num in enumerate(nums):
            helper(nums[i + 1:], path + [num], k - 1, ret)

    ret = []
    nums = range(1, n + 1)
    helper(nums, [], k, ret)
    return ret