#"31[ab22[c]]"

def decodeString(s):
    stack = [["", 0]]
    num = ""
    for c in s:
        if c.isdigit():
            num += c
        elif c == '[':
            stack += ["", int(num)],
            num = ""
        elif c == ']':
            st,k = stack.pop()
            stack[-1][0] += st*k
        else:
            stack[-1][0] += c

    return stack[0][0]


s = "3[a]2[b4[F]c]"
#s = '3[a2[c]]'
#s = '2[abc]3[cd]ef'
#s = '3[a]2[bc]'
#s = "1[a]"
print decodeString(s)
