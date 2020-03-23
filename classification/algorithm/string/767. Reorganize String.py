'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
'''

import collections
def reorganizeString(S):
    counter = collections.Counter(S)
    pairs = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    N = len(pairs)

    def helper(i, remainSlot, leftCnt, strIdx, path):
        if i == N - 1 and leftCnt == 0:
            return path

        if remainSlot == 0:
            if leftCnt == 0:
                ret = helper(i + 1, pairs[i + 1][1], pairs[i + 1][1], 1, path)
            else:
                ret = helper(i, pairs[i][1], leftCnt, 1, path)
        elif leftCnt == 0:
            ret = helper(i + 1, remainSlot, pairs[i + 1][1], strIdx, path)
        else:
            path = path[:strIdx] + pairs[i][0] + path[strIdx:]
            ret = helper(i, remainSlot - 1, leftCnt - 1, strIdx + 2, path)
        return ret

    if len(pairs) == 1:
        return "" if pairs[0][1] > 1 else pairs[0][0]

    ret = helper(1, pairs[0][1], pairs[1][1], 1, pairs[0][0] * pairs[0][1])
    return "" if ret[-1] == ret[-2] else ret

def reorganizeString_slice(S):
    N = len(S)
    A = []
    for c, x in sorted((S.count(x), x) for x in set(S)):
        if c > (N + 1) / 2: return ""
        A.extend(c * x)
    ans = [None] * N
    ans[::2], ans[1::2] = A[N / 2:], A[:N / 2]
    return "".join(ans)

S = "aaabb"
print(reorganizeString_slice(S))

