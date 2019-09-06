def smallestSubsequence(text):
    stack = []
    for i,c in enumerate(text):
        if c in stack: continue

        while stack and c<stack[-1] and stack[-1] in text[i+1:]:
            stack.pop()

        stack += c,

    return "".join(stack)

text = "cdadabccaaccddjjsssdaadfadfeafdsdaewajzdfad"
print smallestSubsequence(text)


