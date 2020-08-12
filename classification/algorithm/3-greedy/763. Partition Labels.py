'''
A string S of lowercase English letters is given.
We want to partition this string into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''

def partitionLabels(S):
    cdict = {c: i for i, c in enumerate(S)}
    ret = []
    largestIdx = anchor = 0
    for i, c in enumerate(S):
        if cdict[c] == i and i >= largestIdx:
            ret.append(i - anchor + 1)
            anchor = i + 1
        largestIdx = max(largestIdx, cdict[c])
    return ret

s = "ababcbacadefegdehijhklij"
print partitionLabels(s)