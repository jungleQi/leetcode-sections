#coding=utf-8

'''
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''

#临界点策略(不好控制，deprecate):
#添加新元素之后，滑动窗口的内容与临界点的关系，来触发不同的行为：
#1.如果窗口内容刚好达到临界点，就比较一次长度；如果窗口内容超出临界点，就按照一定算法来收缩窗口的左边界，
# 为下一次可能的更短长度做准备

#窗口内部只给一个状态：是否覆盖tdict

from collections import Counter


def minWindow(s, t):
    tdict = Counter(t)
    win_cnt = {}
    formed, required = 0, len(tdict)
    left = 0

    ans = float("inf"), None, None
    for right,c in enumerate(s):
        win_cnt[c] = win_cnt.get(c, 0)+1
        if win_cnt[c] == tdict[c]:
            formed += 1

        while formed == required:
            if right-left+1 < ans[0]:
                ans = right-left+1, left, right

            curchar = s[left]
            if curchar not in tdict:
                left += 1
                continue

            win_cnt[curchar] -= 1
            if win_cnt[curchar] < tdict[curchar]:
                formed -= 1
            left += 1

    return s[ans[1]:ans[2]+1] if ans[0] != float("inf") else ""

#s = "ADOBECODEBANCBA"
s = "BAC"
t = "ABC"
print(minWindow(s, t))

