#coding=utf-8

'''
Given an array nums of n integers and an integer target,
are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

#normal: 1. 用 if i>0 and nums[i-1] == nums[i]: continue 来防止duplicate result
#        2. 利用第三层循环的l,r来确定结果；
#        3. 每层循环通过边界元素的sum和target的比较，判断是否需要结束循环

def fourSum_normal(nums, target):
    ret = []
    N = len(nums)
    nums.sort()

    for i in range(N-3):
        if nums[i]*4>target: break
        if i>0 and nums[i-1] == nums[i]: continue
        for j in range(i+1,N-2):
            if nums[i]+nums[j]*3>target: break
            if j>i+1 and nums[j-1] == nums[j]: continue

            l,r = j+1, N-1
            while l<r:
                if nums[i]+nums[j]+2*nums[l]> target or nums[i]+nums[j]+2*nums[r]<target:
                    break

                cursum = nums[i]+nums[j] + nums[l] + nums[r]
                if (l>j+1 and nums[l]==nums[l-1]) or cursum < target:
                    l += 1
                elif (r<N-1 and nums[r]==nums[r+1]) or cursum > target:
                    r -= 1
                else:
                    ret += [nums[i], nums[j],nums[l],nums[r]],
                    l += 1
                    r -= 1
    return ret

target = 11
nums = [0,1,5,0,1,5,5,-4]
print(fourSum_normal(nums, target))


