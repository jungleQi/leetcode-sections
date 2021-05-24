def jump(nums):
    N = len(nums)
    step = curIdx = 0
    while curIdx < len(nums)-1:
        step += 1
        if(curIdx+nums[curIdx] >= N-1): return step

