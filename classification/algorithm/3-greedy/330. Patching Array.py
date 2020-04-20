def minPatches(nums, n):
    ret = 0
    N = len(nums)
    i, reach, curSum = 0, 1, 0
    while reach <= n:
        if i >= N or reach < nums[i]:
            ret += 1
            curSum += reach
            reach = curSum+1
        else:
            curSum += nums[i]
            if curSum >= reach:
                reach = curSum+1
            i = i + 1

    return ret

nums = [1,2,2]
n = 5
print minPatches(nums, n)
