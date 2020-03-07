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

