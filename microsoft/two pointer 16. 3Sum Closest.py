def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    ans = []
    N = len(nums)
    for i in range(N - 2):
        l, r = i + 1, N - 1
        if nums[i] + nums[l] + nums[l + 1] > target:
            ans.append(nums[i] + nums[l] + nums[l + 1])
            break
        elif nums[i] + nums[r - 1] + nums[r] < target:
            ans.append(nums[i] + nums[r - 1] + nums[r])
        else:
            while l < r:
                cursum = nums[i] + nums[l] + nums[r]
                if cursum == target:
                    return cursum
                elif cursum > target:
                    r = r - 1
                else:
                    l = l + 1
                ans.append(cursum)

    ans.sort(key=lambda x: abs(x - target))
    return ans[0]