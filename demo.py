import collections

def removeDuplicateLetters(s):
    counter = collections.Counter(s)
    stack = []
    for c in s:
        while stack and stack[-1] > c and counter[stack[-1]] > 0 and c not in stack:
            stack.pop()
        if c not in stack:
            stack.append(c)
        counter[c] -= 1

    return "".join(stack)

s = "bddbccd"
print(removeDuplicateLetters(s))