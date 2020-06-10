def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxProd = minProd = ans = nums[0]

    for num in nums[1:]:
        minProd, maxProd = min(minProd * num, maxProd * num, num), max(minProd * num, maxProd * num, num)
        ans = max(maxProd, ans)
    return ans
