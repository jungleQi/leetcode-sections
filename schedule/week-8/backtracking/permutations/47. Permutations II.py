#coding=utf-8

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

#time complexity: O(n!)

def permuteUnique_fast(nums):
    def _helper(nums, indexs, path, ret):
        if not nums:
            ret += path,
            return

        for i,num in enumerate(nums):
            if (i>0 and nums[i-1] == num): continue
            _helper(nums[:i]+nums[i+1:], indexs+[i], path+[num], ret)

    ret = []
    nums.sort()
    _helper(nums, [], [], ret)
    return ret

nums = [1,1,2]
print(permuteUnique_fast(nums))

