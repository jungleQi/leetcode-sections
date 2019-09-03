def lengthOfLongestSubstring(s):
    li, ri = 0,0
    longestLen, curLen = 0, 0
    N = len(s)
    while ri<N:
        j = s[li:ri].find(s[ri])
        if j != -1:
            li += j+1
            curLen = ri-li+1
        else:
            curLen += 1
        longestLen = max(longestLen, curLen)

        ri += 1

    return longestLen

s = "bbbbb"
print lengthOfLongestSubstring(s)
#pwwkew
