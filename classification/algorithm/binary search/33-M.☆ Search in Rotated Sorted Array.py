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

        # 注意 "=" 的选择 与 le/ri 增减的关系
        if nums[mid] < nums[ri]:
            if nums[mid] < target and target <= nums[ri]:
                le = mid + 1
            else:
                ri = mid - 1
        else:
            if nums[le] <= target and target < nums[mid]:
                ri = mid - 1
            else:
                le = mid + 1
    return -1