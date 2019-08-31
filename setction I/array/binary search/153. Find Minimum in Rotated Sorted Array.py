def findMin(nums):
    cnt = len(nums)
    left, right = 0, cnt-1

    if nums[0] < nums[-1]:
        return nums[left]
    if (cnt ==2 and nums[left] > nums[left+1]) or \
        (cnt > 2 and nums[left] > nums[left+1] and nums[left+1] > nums[left+2]):
        return nums[-1]

    while left<right:
        mid = (left+right)//2
        if nums[mid] == nums[left]:

            return nums[right]
        elif nums[mid] > nums[left]:
            left = mid
        else:
            right = mid

    return nums[left]

nums = [3,1,2]
print findMin(nums)