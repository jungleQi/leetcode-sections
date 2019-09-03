def minAddToMakeValid(S):
    stack = []
    for char in S:
        if stack and stack[-1] == '(' and char == ')':
            stack.pop()
        else:
            stack.append(char)

    return len(stack)

S = ""
print minAddToMakeValid(S)