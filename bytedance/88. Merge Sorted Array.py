#coding=utf-8

#从数组的尾部开始比较，填值
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    i1, i2 = m - 1, n - 1
    curidx = m + n - 1

    while i1 >= 0 and i2 >= 0:
        if nums1[i1] >= nums2[i2]:
            nums1[curidx] = nums1[i1]
            i1 -= 1
        else:
            nums1[curidx] = nums2[i2]
            i2 -= 1
        curidx -= 1

    if i2 >= 0:
        nums1[:i2 + 1] = nums2[:i2 + 1]