#coding=utf-8

'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

#list [i:j:-1] 对子区间的逆序，很方便的判断子区间是否palilndrome
#在进入二层遍历前，进行便捷的预判

def minCut_slow(s):
    N = len(s)
    # 加快特殊情况的处理效率
    if N <= 1 or s == s[::-1]: return 0

    dp = [i for i in range(N + 1)]
    i = 1
    while i <= N:
        j = i - 1
        while j >= 0:
            if s[j:i] == s[j:i][::-1]:
                dp[i] = min(dp[i], dp[j] + 1)
            j -= 1
        i += 1
    return dp[-1] - 1

import sys
def minCut(s):
    if not s: return 0
    #两种特殊情况的便捷快速判断
    if s == s[::-1]: return 0
    for i in range(len(s)):
        if s[:i + 1] == s[i::-1] and s[i + 1:] == s[:i:-1]:
            print(i, s[:i + 1], s[i::-1], s[i + 1:], s[:i:-1])
            return 1

    dp = [0] * len(s)
    for i in range(len(s)):
        #进行预判，减少进入二层循环的可能
        if s[:i + 1] == s[i::-1]:
            dp[i] = 0
            continue

        dp[i] = sys.maxsize
        for j in range(1, i + 1):
            if s[j:i + 1] == s[i:j - 1:-1]:
                dp[i] = min(dp[i], dp[j - 1] + 1)
    return dp[-1]

s = "abcb"
print(minCut_slow(s))
