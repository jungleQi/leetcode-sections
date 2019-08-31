def removeDuplicateLetters(s):
    if not s : return ""

    from collections import Counter
    counter = Counter(s)

    stack = []
    for c in s:
        if c not in stack:
            while stack and counter[stack[-1]] >= 1 and stack[-1] > c:
                stack.pop()
            stack.append(c)
        counter[c] -= 1

    return "".join(stack)

s = "cbbbbaaajjjafkaccddac"
print removeDuplicateLetters(s)
#"bajfkcd"

