'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
'''

def lengthOfLIS_dp(nums):
    if not nums: return 0
    N = len(nums)
    dp = [1] * N
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def lengthOfLIS(nums):
    dp = []
    ret = 0
    for n in nums:
        N = len(dp)
        l,r = 0,N-1

        while l<r:
            mid = (l+r)/2
            if dp[mid] < n:
                l = mid+1
            elif dp[mid] == n:
                l = mid
                break
            else:
                r = mid

        if N==0 or (l == N-1 and dp[l] < n):
            dp.append(n)
            ret += 1
        else:
            dp[l] = n

    return ret

nums = [1,3,2]
print lengthOfLIS(nums)

