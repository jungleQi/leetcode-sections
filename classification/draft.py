#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections

def maxProduct(nums):
    minProd, maxProd, maxTotal = nums[0], nums[0], nums[0]
    for num in nums[1:]:
        minProd, maxProd = min(minProd*num, maxProd*num), max(minProd*num, maxProd*num)
        maxTotal = max(minProd, maxProd, maxTotal)
    return maxTotal

nums = [0,2]
print maxProduct(nums)