def isValid(s):
    stack = []
    cDict = {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c in cDict.values():
            stack += c,
        elif stack:
            if stack.pop() != cDict[c]:
                return False
        else:
            return False

    return len(stack) == 0

s = "(){[]}"
print isValid(s)

