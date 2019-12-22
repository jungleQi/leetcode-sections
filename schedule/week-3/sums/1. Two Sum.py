'''
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
'''

#1.use python api
#2.one pass , by recording dict[target-curN] = curIdx,
# judge if curN in dict and get mapping idx

import collections
def twoSum_api(nums, target):
    counter1 = collections.Counter(nums)
    for i,n in enumerate(nums):
        if (target-n != n and counter1[target-n] == 1)\
            or (target-n == n and counter1[target-n] > 1):
            return [i, nums.index(target - n,i+1)]

#elegant solution
def twoSum(nums, target):
    hist = {}
    for i, n in enumerate(nums):
        idx = hist.get(n,-1)
        if idx != -1: return [idx, i]
        hist[target-n] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))