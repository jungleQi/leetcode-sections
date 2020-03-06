def maxProduct(nums):
    prev_min = prev_max = global_max = nums[0]
    for num in nums[1:]:
        minn, maxx = min(num, prev_min*num, prev_max*num), max(num, prev_min*num, prev_max*num)
        prev_min, prev_max, global_max = minn, maxx, max(global_max, maxx)

    return global_max

nums = [2,3,-2,4]
print maxProduct(nums)