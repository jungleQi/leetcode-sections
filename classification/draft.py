#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections
#
#        p     c       n
#   N <- 1  <-   2     NULL


def deleteAndEarn(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    nums = [0] + nums
    N = len(nums)

    counter = collections.Counter(nums)
    earn, delete = [0] * N, [0] * N

    nums.sort()
    for i in range(1, N):
        if nums[i] - nums[i - 1] == 1:
            earn[i] = max(delete[i - 1], earn[i - 1] - counter[nums[i - 1]] * nums[i - 1]) + nums[i]
        elif nums[i] == nums[i - 1]:
            ##
            earn[i] = earn[i - 1] + nums[i]
        else:
            earn[i] = max(delete[i - 1], earn[i - 1]) + nums[i]

        if nums[i] == nums[i - 1]:
            delete[i] = delete[i - 1]
        else:
            delete[i] = max(earn[i - 1], delete[i - 1])

    return max(max(earn), max(delete))

#nums = [2, 2, 3, 3, 3, 4]
nums = [3,3,3,4,2]
print deleteAndEarn(nums)

