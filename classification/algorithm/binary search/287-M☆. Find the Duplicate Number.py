#coding=utf-8

'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
1.You must not modify the array (assume the array is read only).
2.You must use only constant, O(1) extra space.
3.Your runtime complexity should be less than O(n2).
4.There is only one duplicate number in the array, but it could be repeated more than once.
'''

#注意 二分算法的4个主要问题：
# 1. while left < OR <= right
# 2. left = mid+1 or mid
# 3. right = mid-1 or mid
# 4. mid = (le+ri)/2 or (le+ri)/2 + 1

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    N = len(nums)
    lo, hi = 0, N - 1

    while lo < hi:
        mid = (lo + hi) / 2

        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1

        if cnt <= mid:
            lo = mid + 1
        else:
            hi = mid
    return lo