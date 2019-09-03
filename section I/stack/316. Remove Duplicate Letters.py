
def removeDuplicateLetters(s):
    from collections import Counter
    counter = Counter(s)

    stack = []
    for c in s:
        if c not in stack:
            while stack and stack[-1] > c and counter[stack[-1]]:
                stack.pop()
            stack.append(c)

        counter[c] -= 1
    return "".join(stack)



s = "cbacdcbc"
print removeDuplicateLetters(s)