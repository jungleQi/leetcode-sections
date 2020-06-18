def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    visitor = {}
    left = 0
    maxLen = 0
    for i, c in enumerate(s):
        if c in visitor and visitor[c] >= left:
            left = visitor[c] + 1

        visitor[c] = i
        maxLen = max(maxLen, i - left + 1)
    return maxLen