'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

def findMedianSortedArrays(nums1, nums2):
    M,N = len(nums1), len(nums2)
    median1 = median2 = (M+N)/2
    if (M+N) % 2 == 0: median1 = median2-1

    i,j,idx = 0,0,0
    prevNum,curNum = 0,0
    while idx<=median2:
        if i == M:
            prevNum ,curNum = curNum, nums2[j]
            j += 1
        elif j == N:
            prevNum, curNum = curNum, nums1[i]
            i += 1
        else:
            if nums1[i]>nums2[j]:
                prevNum, curNum = curNum, nums2[j]
                j += 1
            else:
                prevNum, curNum = curNum, nums1[i]
                i += 1
        idx += 1

    return curNum if median1 == median2 else (prevNum+curNum)/2.0

nums1 = []
nums2 = [2,5]
print(findMedianSortedArrays(nums1, nums2))