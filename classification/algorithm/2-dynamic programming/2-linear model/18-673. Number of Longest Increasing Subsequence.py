#coding=utf-8
'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
'''

def findNumberOfLIS(nums):
    N = len(nums)
    if N == 0: return 0

    lengthest = [1] * (N)
    count = [1] * (N)
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                if lengthest[j] + 1 > lengthest[i]:
                    lengthest[i] = lengthest[j] + 1
                    count[i] = count[j]
                elif lengthest[j] + 1 == lengthest[i]:
                    count[i] += count[j]
            # 这里没有必要做这个判断，实际上在 nums[j] < nums[i] 里逻辑上已经判断过了
            #elif nums[j] == nums[i]:
            #    if lengthest[j] > lengthest[i]:
            #        lengthest[i] = lengthest[j]
            #        count[i] = count[j]

    longest = max(lengthest)
    return sum([count[i] for i in range(N) if lengthest[i] == longest])

nums = [1,3,5,4,3,4]
print(findNumberOfLIS(nums))