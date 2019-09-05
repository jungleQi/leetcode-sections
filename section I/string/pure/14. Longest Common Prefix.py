def longestCommonPrefix(strs):
    prefix = ""
    if not strs:
        return ""

    lens = []
    for i,s in enumerate(strs):
        if i > 0:
            lens += len(s),

    for i,c in enumerate(strs[0]):
        for j in range(1,len(strs)):
            if i >= lens[j-1] or strs[j][i] != c:
                return prefix

        prefix += c

    return prefix

strs = [""]
print longestCommonPrefix(strs)