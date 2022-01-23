'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.
Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

Example 1:
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
'''

#[20,40,5,30]
#[20,40,5,7,6]

def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    second = float("-INF")

    stack = []

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < second:
            return True
        while stack and stack[-1] < nums[i]:
            second = stack.pop()

        stack.append(nums[i])

    return False
