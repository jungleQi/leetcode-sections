def longestCommonPrefix(strs):
    if not strs: return ""
    if len(strs) == 1: return strs[0]

    prefix = ""
    strs.sort()
    for i,j in zip(strs[0], strs[-1]):
        if i == j: prefix += i
        else: break
    return prefix

strs = ["alower","flow","flight"]
print longestCommonPrefix(strs)