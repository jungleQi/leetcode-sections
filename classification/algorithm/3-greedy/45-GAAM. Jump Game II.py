#coding=utf-8

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
'''

def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    step = 0
    i = 0
    while i < len(nums) - 1:
        step += 1

        #如果以i为起点就能跳到last index，就直接返回，不用寻找它后面最佳的候选
        if i + nums[i] >= len(nums) - 1:
            return step

        #以J为起点能够跳的最远的那个J，为下一个最佳候选
        for j in range(i + 1, i + nums[i] + 1):
            #如果能够跳到last index，就直接返回，避免越界和冗余的计算
            if j + nums[j] >= len(nums) - 1:
                return step + 1

            if j + nums[j] > i + nums[i]:
                i = j
    return step