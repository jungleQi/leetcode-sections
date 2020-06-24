#coding=utf-8

'''
Given an 7-array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s.
If there isn't one, return 0 instead.

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
'''

#Time complexity: O(n). Single iteration of O(n).
#Each element can be visited atmost twice, once by the right pointer(i)
#and (atmost)once by the left pointer.

def minSubArrayLen(s, nums):
    cursum, l, ans = 0, 0, float("inf")
    for r, n in enumerate(nums):
        cursum += n
        while cursum >= s:
            ans = min(ans, r - l + 1)
            cursum -= nums[l]
            l += 1

    return 0 if ans == float("inf") else ans

s = 11
nums = [1]
print(minSubArrayLen(s, nums))