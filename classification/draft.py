#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections
#

def lengthOfLIS(nums):
    N = len(nums)
    dp = [1]*N
    for i in range(1,N):
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp[-1]

#nums = [10,9,2,5,3,7,101,18]
nums = [1,3,6,7,9,4,10,5,6]
print lengthOfLIS(nums)






