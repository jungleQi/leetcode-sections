def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    def helper(nums, path, target, ret):
        if target == 0:
            ret.append(path)
            return
        if target < 0:
            return

        for i, num in enumerate(nums):
            helper(nums[i:], path + [num], target - num, ret)

    ret = []
    helper(candidates, [], target, ret)
    return ret