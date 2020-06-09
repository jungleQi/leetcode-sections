# key points:
# 1.dp[i][j] i->j if construct longest substr , 0:no 1:yes

import collections
def longestSubstring_tle(s, k):
    def isSatisfy(subStr, k):
        counter = collections.Counter(subStr)
        for i, v in counter.items():
            if v < k: return False
        return True

    N = len(s)
    maxLen = 0
    dp = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1):
            if dp[j][i - 1] == True and s[i] in s[j:i]:
                dp[j][i] = True
                maxLen = max(maxLen, i - j + 1)
            else:
                ret = isSatisfy(s[j:i + 1], k)
                if ret:
                    dp[j][i] = True
                    maxLen = max(maxLen, i - j + 1)
    return maxLen