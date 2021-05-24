import collections

#[2,3,1,0,1]
def canJump(nums):
    N = len(nums)
    lastPos = N-1
    for i in range(N-1, -1, -1):
        if i+nums[i] >= lastPos:
            lastPos = i

    return lastPos == 0