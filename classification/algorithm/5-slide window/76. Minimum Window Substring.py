#coding=utf-8

'''
Given a 6-string S and a 6-string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty 6-string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''

#对原始字符串进行滑窗，窗口内采用元素采用字典计数，目标字符串也采用字典计数
#求包含目标字符串的最小窗口，也就是目标字典每个元素都出现在窗口中并且元素的数量都达到
#为了避免每次窗口滑动都对目标字典所有的元素及其计数在窗口字典中确认一次，采用第二层的计数
#即目标required需要多少个字符及计数，和formed窗口字典中满足了的字符及计数
#每次滑动窗口，窗口右侧元素在窗口字典中计数+1，它的如果等于在目标字典的计数，formed += 1
#接着比较required和formed是否相等，相等就有当前最小窗口，然后开始做窗口左端向右的递进


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

