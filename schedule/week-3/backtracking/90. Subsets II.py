#coding=utf-8

'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

#subsets中元素的顺序，不一定是在原始nums中的顺序

def subsetsWithDup(nums):
    n = len(nums)
    ret = []
    nums.sort()

    def _helper(start, curset):
        ret.append(curset)
        for i in range(start, n):
            if i>start and nums[i-1] == nums[i]:
                continue
            _helper(i+1, curset+[nums[i]])

    _helper(0, [])
    return ret

nums = [1,2,2]
print(subsetsWithDup(nums))