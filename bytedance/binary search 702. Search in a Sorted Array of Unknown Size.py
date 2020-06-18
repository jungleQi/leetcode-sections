#coding=utf-8

#key point:
# 1.寻找右边界 如果ri的元素值小于target，就将le=ri，并且ri翻倍

def search(reader, target):
    """
    :type reader: ArrayReader
    :type target: int
    :rtype: int
    """
    le, ri = 0, 1
    while reader.get(ri) < target:
        le = ri
        ri <<= 1

    while le <= ri:
        mid = (le + ri) / 2
        val = reader.get(mid)
        if val == target:
            return mid
        elif val > target:
            ri = mid - 1
        else:
            le = mid + 1
    return -1