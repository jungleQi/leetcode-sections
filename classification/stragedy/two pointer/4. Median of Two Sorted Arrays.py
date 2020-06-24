#-*-coding:utf-8-*-

def findMedianSortedArrays(nums1, nums2):
    cnt1, cnt2 = len(nums1), len(nums2)
    mid = (cnt1+cnt2)/2
    odd = (cnt1+cnt2)%2

    i,idx1,idx2 = 0,0,0
    prevNum, curNum = 0, 0
    #pinpoint
    while i<=mid:
        if idx1<cnt1 and idx2<cnt2:
            if nums1[idx1] <= nums2[idx2]:
                prevNum, curNum = curNum, nums1[idx1]
                idx1 += 1
            else:
                prevNum, curNum = curNum, nums2[idx2]
                idx2 += 1
        elif idx1<cnt1:
            prevNum, curNum = curNum, nums1[idx1]
            idx1 += 1
        else:
            prevNum, curNum = curNum, nums2[idx2]
            idx2 += 1

        i += 1

    if odd :
        return curNum/1.0
    else:
        return (prevNum+curNum)/2.0

nums1 = [1,3,5]
nums2 = [0]
print findMedianSortedArrays(nums1, nums2)