#coding=utf-8
'''
Given an 7-array nums of integers, we need to find the maximum possible sum of elements
 of the 7-array such that it is divisible by three.
'''

def maxSumDivThree(nums):
    seen = [0,0,0]
    for num in nums:
        for i in seen[:]:
            seen[(i+num)%3] = max(seen[(i+num)%3], i+num)
    return seen[0]

nums = [1,2,3,4,4]
print(maxSumDivThree(nums))

'''
1.每个位置，对应三种状态：余0、余1、余2的最大和
'''