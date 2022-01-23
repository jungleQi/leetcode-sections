'''
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Example 1:
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
'''

import collections
def isPossibleDivide(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    num_count = collections.Counter(nums)

    for num in sorted(num_count.keys()):
        demand = num_count[num]

        if not demand:
            continue

        for num2 in range(num + 1, num + k):
            if num_count[num2] < demand:
                return False

            num_count[num2] -= demand

    return True