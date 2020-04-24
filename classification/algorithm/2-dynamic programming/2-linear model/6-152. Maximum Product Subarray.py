'''
Given an integer array nums, find the contiguous subarray
within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
'''

def maxProduct(nums):
    minProd, maxProd, maxTotal = nums[0], nums[0], nums[0]
    for num in nums[1:]:
        minProd, maxProd = min(minProd * num, maxProd * num, num), max(num, minProd * num, maxProd * num)
        maxTotal = max(minProd, maxProd, maxTotal)
    return maxTotal

nums = [2,3,-2,4]
print maxProduct(nums)