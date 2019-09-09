def maxRepOpt1(text):
    import collections
    tdict = collections.defaultdict(list)
    for i,t in enumerate(text):
        tdict[t].append(i)

    maxlen = 1
    for c, idxs in tdict.items():
        i = prevlen = curlen = 1
        connect = False

        while i<len(idxs):
            interv = idxs[i]-idxs[i-1]
            if interv == 1:
                curlen += 1
            else:
                maxlen = max(maxlen, 1+curlen+(prevlen if connect else 0))
                prevlen = curlen
                curlen = 1
                connect = True if interv == 2 else False
            i += 1
        maxlen = max(maxlen, curlen + (prevlen if connect else 0))

    return maxlen

text ="ababa"
print maxRepOpt1(text)