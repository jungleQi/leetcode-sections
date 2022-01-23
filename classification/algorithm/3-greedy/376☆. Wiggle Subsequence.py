#coding=utf-8
'''
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative.
In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences,the first because its first two differences are positive and the second because its last difference is zero.

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
    length = 1
    delta = 0
    for i in range(1, len(nums)):
        #处理对算法主流程的干扰
        if (nums[i] == nums[i - 1]): continue

        #<= 而不是 <，统一头部两个元素的处理逻辑
        if (nums[i] - nums[i - 1]) * delta <= 0:
            length += 1
            delta = nums[i] - nums[i - 1]

    return length