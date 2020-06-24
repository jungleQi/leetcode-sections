#coding=utf-8

#key points: binary search problem
#1. 依据mid和le的大小关系，作为第一层判断，左右半区各是什么特点的排列
#2. target和递增半区间关系，作为第二层判断，如果在递增半区间，就在该区间继续二分；否则只可能落在另外一个半区，做二分

def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    N = len(nums)
    le, ri = 0, N - 1

    while le <= ri:
        mid = (le + ri) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[le]: #[le, mid] 是严格递增区间
            if target >= nums[le] and target <= nums[mid]: #target落在[le, mid]区间
                ri = mid - 1
            else: #target落在[mid, ri]区间
                le = mid + 1
        else:# [mid, ri] 是严格递增区间
            if target <= nums[ri] and target >= nums[mid]:#target落在[mid, ri]区间
                le = mid + 1
            else:#target落在[le, mid]区间
                ri = mid - 1

    return -1