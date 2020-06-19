def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    def getStr(src):
        stack1 = []
        for c in src:
            if c == '#' and stack1:
                stack1.pop()
            elif c != '#':
                stack1.append(c)
        return "".join(stack1)

    return getStr(S) == getStr(T)