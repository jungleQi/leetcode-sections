def searchInsert(nums, target):
    cnt = len(nums)
    lo,hi = 0, cnt-1
    while lo < hi:
        mid = (lo+hi)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid+1
        else:
            hi = mid

    return lo+1 if cnt>0 and nums[lo] < target else lo

nums = [1]
target = 1
print(searchInsert(nums, target))