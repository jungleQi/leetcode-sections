'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''

import collections
def intersection(nums1, nums2):
    counter1 = collections.Counter(nums1)
    counter2 = collections.Counter(nums2)
    res = []
    for n1 in counter1.keys():
        if counter2[n1] >= 1:
            res.append(n1)
    return res

#如果nums1, nums2都是升序，就不用sort，时间复杂度O(n)
def intersection_followup(nums1, nums2):
    nums1.sort()
    nums2.sort()

    i1,i2 = 0, 0
    M,N = len(nums1), len(nums2)
    res = []
    while i1<M and i2<N:
        if nums1[i1] == nums2[i2]:
            res.append(nums1[i1])
            i1 += 1
            while i1>0 and i1<M and nums1[i1] == nums1[i1-1]: i1 += 1
            i2 += 1
            while i2>0 and i2<N and nums2[i2] == nums2[i2 - 1]: i2 += 1
        elif nums1[i1] > nums2[i2]:
            i2 += 1
        else:
            i1 += 1
    return res

nums1 = [9]
nums2 = [9]
print(intersection_followup(nums1, nums2))