def threeSumClosest(nums, target):
    nums.sort()
    closestSum  = nums[0]+nums[1]+nums[2]
    cnt = len(nums)
    for i in range(cnt):
        if nums[i]*3 > target:
            break
        if i>0 and nums[i] == nums[i-1]:
            continue

        l, r= i+1, cnt-1
        while l<r:
            if abs(nums[i] + nums[l] + nums[r] - target) < abs(closestSum - target):
                closestSum = nums[i] + nums[l] + nums[r]

            if nums[l]+nums[r] < target-nums[i]:
                l += 1
            elif nums[l]+nums[r] > target-nums[i]:
                r -= 1
            else:
                return target

    return closestSum

nums = [0,1,2]
target = 0
print(threeSumClosest(nums, target))