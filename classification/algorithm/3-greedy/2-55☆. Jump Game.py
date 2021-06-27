#coding=utf-8

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

# https://leetcode.com/problems/jump-game/solution/

#Memory Limit Exceeded
def canJump_MLE(nums):
    def jump(idx):
        if memo[idx] != UNKNOWN:
            return memo[idx] == GOOD

        furthestJump = min(N - 1, idx + nums[idx])
        for pos in range(idx + 1, furthestJump + 1):
            if jump(pos):
                memo[idx] = GOOD
                return True

        memo[idx] = BAD
        return False

    N = len(nums)
    GOOD, BAD, UNKNOWN = 0, 1, 2
    memo = [UNKNOWN] * N
    memo[-1] = GOOD

    return jump(0)

def canJump_greedy_nograce(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # 每个点能覆盖范围内，选一个能到达最远处的点，作为下一个跳点
    jumpPt = 0
    while jumpPt < len(nums) - 1:
        nextPt = curIdx = jumpPt

        while curIdx < len(nums) and nextPt < len(nums) and curIdx <= nextPt + nums[nextPt]:
            nextPt = max(nextPt, curIdx + nums[curIdx])
            curIdx += 1
        if nextPt <= jumpPt:
            return False
        jumpPt = nextPt

    return True

def canJump_greedy_grace(nums):
    N = len(nums)
    lastpos = N - 1
    for i in range(N - 1, -1, -1):
        if i + nums[i] >= lastpos:
            lastpos = i
    return lastpos == 0


