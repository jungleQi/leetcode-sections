def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    le, ri = 0, len(nums) - 1
    while le <= ri:
        if nums[le] <= nums[ri]:
            return nums[le]
        mid = (le + ri) // 2

        #print le, ri, mid
        if nums[mid] < nums[ri]:
            ri = mid
        else:
            le = mid + 1

nums = [3,4,5,1,2]
print(findMin(nums))