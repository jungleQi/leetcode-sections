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