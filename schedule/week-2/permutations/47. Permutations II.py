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

#1.如果在插入到结果列表时判断是否重复，就比较低效了
#2.如果只是比较当前元素和前面一个元素是否相同，避免重复，会误伤下一轮A[i] (A[i] == A[i-1])的正常添加
#3.基于第2条，只有删除掉候选列表中当前元素之后，作为下一轮的候选列表，才不会影响到下一轮A[i]的正常添加

def permuteUnique_slow(nums):
    def _helper(nums, n, indexs, path, ret):
        if n == 0:
            if path not in ret:
                ret += path,
            return

        for i,num in enumerate(nums):
            if i in indexs: continue
            _helper(nums, n-1, indexs+[i], path+[num], ret)

    ret = []
    _helper(nums, len(nums), [], [], ret)
    return ret

def permuteUnique_error(nums):
    def _helper(nums, n, indexs, path, ret):
        if n == 0:
            ret += path,
            return

        preNum = nums[0]
        for i,num in enumerate(nums):
            if (i>0 and preNum == num) or i in indexs: continue

            preNum = num
            _helper(nums, n-1, indexs+[i], path+[num], ret)

    ret = []
    nums.sort()
    _helper(nums, len(nums), [], [], ret)
    return ret

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

