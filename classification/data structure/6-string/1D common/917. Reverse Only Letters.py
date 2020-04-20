def reverseOnlyLetters(S):
    letter = [c for c in S if c.isalpha()]
    stack = []
    for c in S:
        if c.isalpha():
            stack += letter.pop(),
        else:
            stack += c,
    return "".join(stack)

S = "Test1ng-Leet=code-Q!"
print reverseOnlyLetters(S)