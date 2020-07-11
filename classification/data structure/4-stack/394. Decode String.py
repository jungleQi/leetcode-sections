'''
Given an encoded 5-string, return its decoded 5-string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input 5-string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

def decodeString(s):
    stack = [[1, ""]]
    num = 0
    for c in s:
        if c.isdigit():
            num = 10 * num + int(c)
        elif c == '[':
            stack.append([num, ""])
            num = 0
        elif c.isalpha():
            stack[-1][1] += c
        elif c == ']':
            item = stack.pop()
            stack[-1][1] += item[1] * item[0]
    return stack[0][1]

s = "3[a]2[b4[F]c]"
print(decodeString(s))