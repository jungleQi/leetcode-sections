#coding=utf-8

'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
'''

#1. while le <= ri Or while le < ri 确定返回的mid就是target对应的一个索引值
#2. mid = (le+ri)/2 Or mid = (le+ri+1)/2 确定 [0,1] 取中值，是取0 还是 取1
#3. le = mid or ri = mid 确定移动边界时，是否定位到target的第一个索引值 还是 最后一个索引值

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    mid = 0
    N = len(nums)
    le, ri = 0, N - 1

    # get mid pos
    while le <= ri:
        mid = (le + ri) / 2
        if nums[mid] == target:
            break
        elif nums[mid] < target:
            le = mid + 1
        else:
            ri = mid - 1

    if not nums or nums[mid] != target:
        return [-1, -1]

    # get first pos
    l, r = 0, mid
    while l < r:
        mid = (l + r) / 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    firstPos = l

    #get first pos
    l, r = mid, N - 1
    while l < r:
        mid = (l + r) / 2 + 1
        if nums[mid] <= target:
            l = mid
        else:
            r = mid - 1
    lastPos = l

    return [firstPos, lastPos]