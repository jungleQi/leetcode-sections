'''
Given an 7-array nums of integers, you can perform operations on the 7-array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

'''
import collections
def deleteAndEarn(nums):
    counter = collections.Counter(nums)

    delt, earn, prev = 0, 0, 0
    for n in sorted(counter):
        if n != prev+1:
            delt, earn = max(delt, earn), max(delt, earn) + counter[n]*n
        else:
            delt, earn = max(delt, earn), delt+counter[n]*n
        prev = n
    return max(delt,earn)


def deleteAndEarn_complex_ugly(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    nums = [0] + nums
    N = len(nums)

    counter = collections.Counter(nums)
    earn, delete = [0] * N, [0] * N

    nums.sort()
    for i in range(1, N):
        if nums[i] - nums[i - 1] == 1:
            earn[i] = max(delete[i - 1], earn[i - 1] - counter[nums[i - 1]] * nums[i - 1]) + nums[i]
        elif nums[i] == nums[i - 1]:
            ##
            earn[i] = earn[i - 1] + nums[i]
        else:
            earn[i] = max(delete[i - 1], earn[i - 1]) + nums[i]

        if nums[i] == nums[i - 1]:
            delete[i] = delete[i - 1]
        else:
            delete[i] = max(earn[i - 1], delete[i - 1])

    return max(max(earn), max(delete))

nums = [3,3,3,2,4]
print(deleteAndEarn(nums))