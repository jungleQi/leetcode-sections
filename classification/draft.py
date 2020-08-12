def partitionLabels(S):
    cdict = {c:i for i,c in enumerate(S)}
    ret = []
    largestIdx = anchor = 0
    for i, c in enumerate(S):
        if cdict[c] == i and i >= largestIdx:
            ret.append(i-anchor+1)
            anchor = i+1
        largestIdx = max(largestIdx, cdict[c])
    return ret

S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))