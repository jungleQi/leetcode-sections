def findMin(nums):
    cnt = len(nums)
    left, right = 0, cnt-1

    if cnt == 1:
        return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]

    if (cnt ==2 and nums[0]>nums[1]) or (cnt > 2 and nums[0] > nums[1] and nums[1]>nums[2]):
        return nums[-1]

    while left < right:
        mid = (left+right)//2

        if mid == left:
            return nums[right]

        if nums[mid] == nums[left]:
            if nums[left] <= nums[left+1]:
                left += 1
            else:
                return nums[left+1]
        elif nums[mid] > nums[left]:
            left = mid
        else:
            right = mid

nums = [5,5,6,7,1,2,2]
print(findMin(nums))