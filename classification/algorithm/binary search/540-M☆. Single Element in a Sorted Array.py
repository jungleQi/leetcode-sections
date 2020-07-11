#coding=utf-8

'''
You are given a sorted array consisting of only integers where every element appears exactly twice,
except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
'''

#1.二分在大的方向上是否能够逐步缩小目标的查找范围
#2.收敛结束的条件设定
#3.[0,1]取中值，mid是定位到 0 or 1
#4.le/ri依据mid进行合理的移动

def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    le, ri = 0, len(nums) - 1
    while le < ri:
        mid = (le + ri + 1) / 2

        if (mid - le) % 2 == 0:
            if nums[mid] == nums[mid - 1]:
                ri = mid - 1
            else:
                le = mid
        else:
            if nums[mid] == nums[mid - 1]:
                le = mid + 1
            else:
                ri = mid - 1
    return nums[le]

def singleNonDuplicate_concise(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    l, h = 0, N - 1

    while l < h:
        mid = (h + l) / 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            l = mid + 2
        else:
            h = mid
    return nums[l]