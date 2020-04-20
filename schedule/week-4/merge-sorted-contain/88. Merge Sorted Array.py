#coding=utf-8

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted 7-array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

#从尾部开始比较，比较nice

def merge(nums1, m, nums2, n):
    j = 0
    end = len(nums1)
    for i,v in enumerate(nums2):
        while j<m+i and nums1[j]<=v: j += 1
        if j == m+i:
            nums1[j:j+n-i] = nums2[i:n]
            break
        else:
            nums1[j+1:end] = nums1[j:end-1]
            nums1[j] = v

#elegant
def merge_fromEnd(nums1, m, nums2, n):
    end = m+n-1
    i1, i2 = m-1, n-1
    while i1 >= 0 and i2 >= 0:
        if nums1[i1] > nums2[i2]:
            nums1[end] = nums1[i1]
            i1 -= 1
        else:
            nums1[end] = nums2[i2]
            i2 -= 1
        end -= 1

    if i1 < 0:
        nums1[:i2+1] = nums2[:i2+1]


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [-1,3,4]
n = 3
merge_fromEnd(nums1, m, nums2, n)
print(nums1)

