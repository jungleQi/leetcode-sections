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


nums = [3,3,3,2,4]
print(deleteAndEarn(nums))