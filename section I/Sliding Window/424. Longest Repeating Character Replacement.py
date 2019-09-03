def characterReplacement(s, k):
    sRear = len(s)-1

    def getMaxLen(idxs):
        consumePadding = [0]
        curPadding, N = 0, len(idxs)
        for i in range(1, N):
            curPadding += idxs[i] - idxs[i - 1] - 1
            consumePadding.append(curPadding)

        maxLen = 0
        li, ri = 0, 0
        while li <= ri and ri < N:
            remainPadding = consumePadding[ri] - consumePadding[li]
            if remainPadding <= k:
                delta = k - remainPadding

                delta = delta if idxs[li]+sRear-idxs[ri] >= delta else sRear-idxs[ri]
                curLen = idxs[ri] - idxs[li] + 1 + delta

                maxLen = max(maxLen, curLen)
                ri += 1
            else:
                li += 1
        return maxLen

    cdict = dict()
    for i, c in enumerate(s):
        if c not in cdict:
            cdict[c] = [i]
        else:
            cdict[c].append(i)

    maxlen = 0
    for c, idxs in cdict.items():
        maxlen = max(maxlen, getMaxLen(idxs))

    return maxlen

s = "ABABAAABBBCAABBBAABBAAAABBBBCCCCCCCDDCC"
k = 3
print characterReplacement(s, k)
