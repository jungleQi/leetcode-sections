#coding=utf-8

'''
You are given a 6-string, s, and a list of words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in
words exactly once and without any intervening characters.

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]

'''

#couting in sliding window
#先对窗口win(窗口长度为len(words))内的字符及其个数与word进行一次比较
#如果win字典 == word字典，才进行每段单词的依次比较；否则窗口滑动到下一个，做一次两端元素的字典增减

import collections, copy

def findSubstring(s, words):
    wordCnt = len(words)
    if wordCnt == 0: return []
    wordLen = len(words[0])
    if wordLen == 0: return []
    l, start, N = 0, wordLen*wordCnt,len(s)
    if N == 0 or start > N: return []

    out = []
    tDict = collections.Counter("".join(words))
    sDict = collections.Counter(s[:start])
    for r in range(start, N+1):
        if tDict == sDict:
            i,ll = 0,l
            wordDict = collections.Counter(words)
            while i<wordCnt:
                curstr = s[ll:ll+wordLen]
                if wordDict[curstr] == 0: break
                wordDict[curstr] -= 1

                ll += wordLen
                i += 1
            if sum(wordDict.values()) == 0:
                out += l,

        if r == N : break
        sDict[s[r]] += 1
        sDict[s[l]] -= 1
        if sDict[s[l]] == 0: del sDict[s[l]]
        l += 1

    return out

s = ""
words = ["foo","bar"]
print(findSubstring(s, words))