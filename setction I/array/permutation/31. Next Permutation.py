def nextPermutation(nums):
    def binary_find(nums, left, right, target):
        oriLeft = left
        while left < right:
            mid = (left + right) / 2
            if nums[mid]>target:
                left = mid+1
            elif nums[mid]<target:
                right = mid-1
            else:
                curRight = mid-1
                while oriLeft < curRight:
                    if nums[curRight] > target:
                        break
                    curRight -= 1
                return curRight

        return left if nums[left] > target else left-1

    adjustIdx, numCnt = -1, len(nums)
    for i in range(numCnt-1, 0, -1):
        if nums[i] > nums[i-1]:
            adjustIdx = i-1
            break

    if adjustIdx == -1:
        nums.reverse()
        return

    left, right = adjustIdx + 1, numCnt - 1
    swapIdx = binary_find(nums, left, right, nums[adjustIdx])
    print(adjustIdx, left, right, swapIdx)
    nums[adjustIdx], nums[swapIdx] = nums[swapIdx], nums[adjustIdx]

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return

def nextPermutation2(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 1
    low_id = -1
    low = nums[-1]

    while i > 0:
        if nums[i] > nums[i - 1]:
            #if nums[i] < low:
            #    low = nums[i]
            #    low_id = i
            while nums[i - 1] >= low:
                low_id -= 1
                low = nums[low_id]

            nums[low_id], nums[i - 1] = nums[i - 1], nums[low_id]
            nums[i:] = nums[i:][::-1]
            break

        #if nums[i] < low:
        #    low = nums[i]
        #    low_id = i

        i -= 1

    if i == 0:
        nums.reverse()

nums = [2,2,7,5,4,3,2,2,1]
nextPermutation2(nums)
print(nums)