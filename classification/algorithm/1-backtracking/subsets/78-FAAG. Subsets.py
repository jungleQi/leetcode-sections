#coding=utf-8

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


#1.循环体对ret[::]操作，避免对ret自身操作，导致无限循环
#2.递归解决类似问题，比较普适

def subsets(nums):
    ret = [[]]
    for i, n in enumerate(nums):
        for item in ret[::]:
            ret.append(item + [n])
    return ret

def subsets_rec(nums):
    def helper(nums, cur, ret):
        ret.append(cur)
        if not nums: return
        for i, num in enumerate(nums):
            helper(nums[i + 1:], cur + [num], ret)

    ret = []
    helper(nums, [], ret)
    return ret

nums = [1,2,3]
print(subsets_rec(nums))