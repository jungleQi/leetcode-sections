#coding=utf-8

import collections
def lengthOfLongestSubstringTwoDistinct(s):
    """
    :type s: str
    :rtype: int
    """
    N = len(s)
    if N < 3: return N

    left = right = 0
    hashmap = collections.defaultdict()
    maxLen = 1

    for i in range(N):
        right += 1

        if len(hashmap) < 3:
            hashmap[s[i]] = i

        if len(hashmap) == 3:
            idx = min(hashmap.values())
            del hashmap[s[idx]]
            #因为hashmap的更新规律与特点，这里直接+1处理，就能得到下一个字符的起始索引值
            left = idx + 1

        maxLen = max(maxLen, right - left)
    return maxLen