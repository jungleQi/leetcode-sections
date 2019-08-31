def scoreOfParentheses(S):
    stack = [0]  # The score of the current frame

    for char in S:
        if char == '(':
            stack.append('(')
            continue

        if stack[-1] == '(':
            # ((, 5(
            stack.pop()
            if stack[-1] == '(':
                stack += 1,
            else:
                stack[-1] += 1
        else:
            curv = stack.pop()
            stack.pop()
            if stack[-1] == '(':
                stack += 2*curv,
            else:
                stack[-1] += 2*curv

    return stack.pop()


S = "()"
print scoreOfParentheses(S)