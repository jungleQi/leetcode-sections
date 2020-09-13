#coding=utf-8
'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative.
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence.
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence,
leaving the remaining elements in their original order.

Example 1:
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
'''


def wiggleMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)

    prevDiff = nums[1] - nums[0]
    cnt = 2 if prevDiff != 0 else 1

    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        # 这里的条件判断很优雅
        if (diff > 0 and prevDiff <= 0) or (diff < 0 and prevDiff >= 0):
            cnt += 1
            prevDiff = diff
    return cnt