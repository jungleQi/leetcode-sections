'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

#如果将Num和str间隔入栈，整体流程会非常混乱
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
            n = stack.pop()
            stack[-1] += cur*n
            cur = ""
    return cur if cur else stack[-1]

#只有采用[num, str]的结构入栈，才能保证处理流程清晰
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

s = "3[a]2[b4[F]c]"
print(decodeString(s))