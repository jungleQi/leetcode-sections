def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    le, ri = 0, len(height) - 1

    maxVal = 0
    while le < ri:
        maxVal = max(maxVal, (ri - le) * min(height[le], height[ri]))

        if height[le] < height[ri]:
            le += 1
        else:
            ri -= 1
    return maxVal