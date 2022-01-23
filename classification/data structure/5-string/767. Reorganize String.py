#coding=utf-8

'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""
'''

def reorganizeString_I(S):
    N = len(S)
    A = []
    for i, x in sorted((S.count(x), x) for x in set(S)):
        if i > (N + 1) // 2: return ""
        A.extend([x] * i)

    ans = [None] * N
    ans[::2] = A[N // 2:]
    ans[1::2] = A[:N // 2]
    return "".join(ans)

import heapq
def reorganizeString_II(S):
    #用插入的方式不优雅，数组元素需要批量移动
    # 实际上是对堆的熟练运用, 为什么是greedy，不太理解
    sdict = [(-S.count(c), c) for c in set(S)]
    if any(-nc > (len(S) + 1) / 2 for nc, x in sdict):
        return ""

    heapq.heapify(sdict)

    ret = []
    while (len(sdict) >= 2):
        nct1, ch1 = heapq.heappop(sdict)
        nct2, ch2 = heapq.heappop(sdict)
        ret.extend([ch1, ch2])

        nct1 += 1
        nct2 += 1
        if nct1 != 0: heapq.heappush(sdict, (nct1, ch1))
        if nct2 != 0: heapq.heappush(sdict, (nct2, ch2))
    return "".join(ret) + (sdict[0][1] if sdict else "")