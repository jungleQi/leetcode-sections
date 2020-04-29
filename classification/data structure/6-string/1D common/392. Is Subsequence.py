def isSubsequence(s, t):
    i = -1
    for ch in s:
        i = t.find(ch, i + 1)
        if i == -1:
            return False
    return True

s = "axc"
t = "ahbgdc"
print(isSubsequence(s, t))