def sortColors_concise(nums):
        p0 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] == 0:
            l += 1
        elif nums[r] == 2:
            r -= 1
        else:

            if nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            elif nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            else:
                cur = l
                while cur < r:
                    if nums[cur] == 0:
                        nums[l], nums[cur] = nums[cur], nums[l]
                        l += 1
                        break
                    elif nums[cur] == 2:
                        nums[r], nums[cur] = nums[cur], nums[r]
                        r -= 1
                        break
                    cur += 1
                if cur == r: break