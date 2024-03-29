'''
From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target.
If the task is impossible, return -1.

Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
'''

def shortestWay(source, target):
    """
    :type source: str
    :type target: str
    :rtype: int
    """
    subseqCnt, targetIdx = 0, 0
    while targetIdx < len(target):
        srcIdx = 0
        srcSeq = False

        while srcIdx < len(source) and targetIdx < len(target):
            if source[srcIdx] == target[targetIdx]:
                srcIdx += 1
                targetIdx += 1
                srcSeq = True
            else:
                srcIdx += 1

        if not srcSeq: return -1
        subseqCnt += 1
    return subseqCnt

import collections
def shortestWay_quick(source, target):
    def find(idxs, i):
        for j in idxs:
            if j>i: return j
        return -1

    cdict = collections.defaultdict(list)
    for i,s in enumerate(source):
        cdict[s].append(i)

    cnt, over = 0, True
    for i, c in enumerate(target):
        if over :
            start = cdict[c][0]
            over = False
            cnt += 1
        else:
            start = find(cdict[c], start)
            if start == -1:
                over = True
    return cnt