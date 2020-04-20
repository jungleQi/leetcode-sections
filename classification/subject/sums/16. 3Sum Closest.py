#coding=utf-8

'''
Given an 7-array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example:
Given 7-array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

#normal：第二层循环采用l,r两个端点，依据triplet sum 和target的大小，判断如何移动l或者r

#optimize：在进行第二次循环之前，先判断n+num[l]+num[l+1] 或者n+nums[r-1]+nums[r]
# 这两种终端case和target的大小关系，避免所有case都进入第二层循环

import sys
def threeSumClosest_normal(nums, target):
    N, nearestSum = len(nums), sys.maxsize
    nums.sort()

    for i in range(N-2):
        tar = target - nums[i]
        l,r = i+1,N-1
        while l<r:
            cursum = nums[i] + nums[l] + nums[r]
            if abs(cursum-target) < abs(nearestSum-target):
                nearestSum = cursum

            if nums[l]+nums[r] == tar:
                return target
            elif nums[l]+nums[r] > tar:
                r -= 1
            else:
                l += 1

    return nearestSum

def threeSumClosest_opt(nums, target):
    N = len(nums)
    ret = []
    nums.sort()

    for i in range(N-2):
        l,r = i+1,N-1
        if nums[i]+nums[l]+nums[l+1] > target:
            ret.append(nums[i]+nums[l]+nums[l+1])
        elif nums[i]+nums[r-1]+nums[r] < target:
            ret.append(nums[i]+nums[r-1]+nums[r])
        else:
            while l<r:
                cursum = nums[i]+nums[l]+nums[r]
                if cursum == target:
                    return target
                elif cursum < target:
                    l+=1
                else:
                    r-= 1
                ret.append(cursum)

    ret.sort(key=lambda x:abs(x-target))
    return ret[0]

nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest_opt(nums, target))