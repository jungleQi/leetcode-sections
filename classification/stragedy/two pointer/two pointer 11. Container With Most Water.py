def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height) - 1
    maxVal = 0
    while l < r:
        if height[l] < height[r]:
            if maxVal < height[l] * (r - l):
                maxVal = height[l] * (r - l)
            l += 1
        else:
            if maxVal < height[r] * (r - l):
                maxVal = height[r] * (r - l)
            r -= 1
    return maxVal