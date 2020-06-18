#coding=utf-8

#key point:
# 1.从尾部向头部一次遍历，第一个出现变小的数字，就是需要交换的点
# 2.从需要交换的点P，向尾部遍历，寻找最后一个比P大的点Q，交换P和Q
# 3.对[P+1, end]之间的元素，进行倒置交换

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    N = len(nums)
    if N <= 1: return

    #是否交换过
    isRev = False
    for i in range(N - 2, -1, -1):
        # 交换时机
        if nums[i] < nums[i + 1]:
            j = i + 1
            while j < N:
                if nums[j] <= nums[i]: break
                j += 1

            nums[i], nums[j - 1] = nums[j - 1], nums[i]
            isRev = True
            break

    #如果没有交换，就整体倒置
    if not isRev:
        nums.reverse()
    else:
        #倒置交换起始点之后区域，保证 next greater permutation
        le, ri = i + 1, N - 1
        while le < ri:
            nums[le], nums[ri] = nums[ri], nums[le]
            le += 1
            ri -= 1