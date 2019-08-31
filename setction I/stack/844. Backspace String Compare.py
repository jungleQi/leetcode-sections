def backspaceCompare(S, T):
    def getFinalStr(str):
        stack = []
        for c in str:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return "".join(stack)

    return getFinalStr(S) == getFinalStr(T)

S ="ac#"
T ="a"
print(backspaceCompare(S, T))
