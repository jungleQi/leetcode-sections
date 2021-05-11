def decodeString_failed(s):
    num = 0
    stack = [""]
    cur = ""
    for c in s:
        if c.isdigit():
            if cur:
                stack.append(cur)
                cur = ""
            num += 10*num + int(c)
        elif c.isalpha():
            cur += c
        elif c == '[':
            stack.append(num)
            num = 0
        elif c == ']':
            print(stack)
            n = stack.pop()
            stack[-1] += cur*n
            cur = ""
    return cur if cur else stack[-1]

def decodeString(s):
    stack = [[1,""]]
    num = 0
    for c in s:
        if c.isdigit():
            num = 10*num+int(c)
        elif c.isalpha():
            stack[-1][1] += c
        elif c == '[':
            stack.append([num, ""])
            num = 0
        elif c == ']':
            element = stack.pop()
            stack[-1][1] += element[1]*element[0]
    return stack[0][1]

s = "10[le]"
print(decodeString(s))