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
    def helper(nums, cur, ret):
        if not nums:
            ret.append(cur)
            return

        for i,num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            helper(nums[:i]+nums[i+1:], cur+[num], ret)

    nums.sort()
    ret = []
    helper(nums, [], ret)
    return ret

nums = [1,1,2]
print(permuteUnique_fast(nums))

