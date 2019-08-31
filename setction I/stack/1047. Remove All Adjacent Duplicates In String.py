def removeDuplicates(S):
    stack = []
    for c in S:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack += c,

    return "".join(stack)

S = "aabbacca"
print(removeDuplicates(S))