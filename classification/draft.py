import collections
def smallestSubsequence(text):
    """
    :type text: str
    :rtype: str
    """
    stack = []
    for i, c in enumerate(text):
        if c in stack: continue
        if stack and c<stack[-1] and stack[-1] in text[i:]:
            stack.pop()

        stack += c,
    return stack
