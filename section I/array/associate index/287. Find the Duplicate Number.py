def findDuplicate(nums):
    lo,hi  = 1, len(nums)

    while lo<hi:
        mid = (lo+hi)/2

        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1

        if cnt > mid:
            hi = mid
        else:
            lo = mid+1

    return lo

nums = [1,3,4,2,2]
print findDuplicate(nums)