import collections
def maximumSwap(num):
    """
    :type num: int
    :rtype: int
    """
    nums = list(str(num))
    numIdx = collections.defaultdict(list)
    for i, n in enumerate(nums):
        numIdx[n].append(i)

    for i, n in enumerate(nums):
        if not nums[i + 1:]:
            break
        maxNum = max(nums[i + 1:])
        if maxNum > n:
            idx = max(numIdx[maxNum])
            nums[i], nums[idx] = nums[idx], nums[i]
            return int("".join(nums))

    return num