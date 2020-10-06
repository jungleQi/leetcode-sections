#coding=utf-8
'''
Given an array nums sorted in ascending order,
return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
'''

import collections
def isPossible(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    num_count = []
    #将item的类型由tuple转换成list，便于后面对item[1]进行递减操作
    for item in collections.Counter(nums).items():
        num_count.append(list(item))

    numItems = sorted(num_count, key=lambda x: x[0])

    i = 0
    while i < len(numItems):
        if numItems[i][1] == 0:
            i += 1
            continue
        #从有效的第一个数开始计算
        numItems[i][1] -= 1
        cnt = 1

        j = i + 1
        # greedy：当前数比前序数大1(contineous) 而且 当前数的剩余个数大于前序数时，将当前数剩余个数-1，一直向后保持contineous
        # 大小相邻的前序数和当前数的数目关系的判断是greedy算法生效的关键，比如[1,2,3,3,4,5]
        while j < len(numItems):
            if numItems[j][1] <= numItems[j - 1][1] or numItems[j][0] - numItems[j - 1][0] != 1:
                break
            numItems[j][1] -= 1
            cnt += 1
            j += 1
        #如果该轮subsequence能够contineous的数目不足3，就返回
        if cnt < 3: return False

    return True

nums = [10,2,2,3,3]
isPossible(nums)