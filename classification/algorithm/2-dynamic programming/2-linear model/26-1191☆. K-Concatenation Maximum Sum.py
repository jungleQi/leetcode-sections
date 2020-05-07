#coding=utf-8

'''
Given an integer array arr and an integer k, modify the array by repeating it k times.
For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array.
Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

Example 1:
Input: arr = [1,2], k = 3
Output: 9
'''

def kConcatenationMaxSum_complex(arr, k):
    def getMaxSubs(arr):
        maxSum = arr[0]
        curSum = 0
        maxStart, maxEnd = 0, 0
        istart, iend = 0, 0
        for i, num in enumerate(arr):
            if curSum < 0:
                istart = iend = i
                curSum = 0

            curSum += num
            iend = i
            if curSum > maxSum:
                maxSum = curSum
                maxStart = istart
                maxEnd = iend

        return maxSum, maxStart, maxEnd + 1

    arrSum = sum(arr)
    arrOneSum, maxStart, maxEnd = getMaxSubs(arr)
    arrTwoSum, _, _ = getMaxSubs(arr * 2)
    mod = 10 ** 9 + 7
    if k == 1:
        return max(0, arrOneSum) % mod
    elif arrSum <= 0:
        return max(0, arrTwoSum) % mod
    else:
        return (sum(arr[maxStart:]) + (k - 2) * arrSum + sum(arr[:maxEnd])) % mod

def kConcatenationMaxSum(arr, k):
    def get_max_sub(a):
        maxsum = cursum = 0
        for v in a:
            cursum += v
            if cursum < 0:
                cursum = 0 if v < 0 else v
            else:
                maxsum = max(maxsum, cursum)
        return maxsum

    if max(arr) <= 0: return 0
    max1 = get_max_sub(arr)
    max2 = get_max_sub(arr*2)
    max3 = sum(arr)
    if max3>0 and k>2:
        #lightspot:
        # arr2 = arr + arr的最大值区间，无论出现在arr2的左端、中端、还是右端，
        # (k-2)*max3都能找到对应的位置，得到下面👇的最大值
        max3 = (k-2)*max3 + max2

    return max(max1,max2,max3) % (10**9 + 7)

arr = [1,-2,1]
k = 5
print kConcatenationMaxSum(arr, k)