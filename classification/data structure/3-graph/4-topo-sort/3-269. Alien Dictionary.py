#coding=utf-8

'''
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
'''

#1. adjacent list + indegree
#2. topo sort

import collections
def alienOrder(words):
    chars = set("".join(words))
    indegree = {c:0 for c in chars}

    #adjacent list：
    letters = collections.defaultdict(set)
    for f, b in zip(words[:-1], words[1:]):
        fl, bl = len(f), len(b)
        minlen = min(fl, bl)

        #["wrtkj","wrt"] 这种case，应该为invalid，需要单独判断
        if f[:minlen] == b[:minlen] and fl > bl: return ""

        for i in range(0, ):
            #特别容易错，此处如果不做判断，会导致相同的pair重复判断，indegree的计算出现错误
            if b[i] in letters[f[i]]:
                break
            if (f[i] != b[i]):
                letters[f[i]].add(b[i])
                indegree[b[i]] += 1
                break

    #initialize indegree：
    deque = collections.deque()
    for k,v in indegree.items():
        if v == 0: deque.append(k)

    #topo sort
    ans = []
    while deque:
        p = deque.popleft()
        ans.append(p)

        for c in letters[p]:
            indegree[c] -= 1
            if indegree[c] == 0:
                deque.append(c)

    return "".join(ans) if len(ans) == len(chars) else ""

words = ["ab","b"]
#words = ["wrt","wrf","er","ett","rftt","te"]
print(alienOrder(words))