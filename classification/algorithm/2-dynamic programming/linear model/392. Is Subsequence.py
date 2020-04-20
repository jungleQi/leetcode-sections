def isSubsequence(s, t):
    if not s:
        return True

    curidx, slen = 0, len(s)
    for c in t:
        if curidx<slen and s[curidx] == c:
            curidx += 1

    return curidx == slen

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))