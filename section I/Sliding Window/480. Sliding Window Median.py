import bisect

def medianSlidingWindow(nums, k):
    win = sorted(nums[:k])
    ret = []
    for a, b in zip(nums, nums[k:]+[0]):
        ret.append( (win[k/2]+win[~(k/2)]) / 2. )
        win.remove(a)
        bisect.insort(win, b)
    return ret

k = 3
nums = [1,3,-1,-3,5,3,6,7]
print medianSlidingWindow(nums, k)