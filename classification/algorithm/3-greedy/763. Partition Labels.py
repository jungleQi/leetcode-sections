
def partitionLabels(S):
    last = {c:i for i,c in enumerate(S)}

    anchor,j = 0,0
    ret = []
    for i,c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            ret.append(j-anchor+1)
            anchor = j+1
    return ret

s = "ababcbacadefegdehijhklij"
print partitionLabels(s)