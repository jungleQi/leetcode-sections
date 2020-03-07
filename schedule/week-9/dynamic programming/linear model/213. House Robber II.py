def rob(nums):
    def _rob(nums, N):
        if N <= 2: return max(nums)

        prev_2 = nums[0]
        prev_1 = max(nums[0],nums[1])
        for num in nums[2:]:
            curmax = max(prev_2+num, prev_1)
            prev_2, prev_1 = prev_1, curmax

        return prev_1

    N = len(nums)
    if N == 0: return 0
    if N == 1: return nums[0]

    oneMax = _rob(nums[:-1], N-1)
    anotherMax = _rob(nums[1:], N-1)
    return max(oneMax, anotherMax)

nums = [1,2,3]
print(rob(nums))