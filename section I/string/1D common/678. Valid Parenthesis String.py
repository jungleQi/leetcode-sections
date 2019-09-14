def checkValidString(s):
    remainCnt =0
    for c in s:
        if c in ['(', '*']:
            remainCnt += 1
        else:
            remainCnt -= 1
        if remainCnt < 0: return False

    remainCnt = 0
    for c in reversed(s):
        if c in [')', '*']:
            remainCnt += 1
        else:
            remainCnt -= 1
        if remainCnt < 0: return False

    return True

#s =  "(*)((*"
#s = "*(()))"
s = "(*))"
print(checkValidString(s))