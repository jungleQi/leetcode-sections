#coding=utf-8

def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    # keypoint:
    # 1. using stack
    # 2. stack item is not single, but ["", number]
    # 3. put stack: when see '['
    # 4. pop stack: when see ']'，after this append the substring to stack top's str

    stack = [["", 0]]
    num = 0
    for c in s:
        if c.isdigit():
            num = 10 * num + int(c)
        elif c == '[':
            stack.append(["", num])
            num = 0
        elif c == ']':
            substr, repeat = stack.pop()
            stack[-1][0] += substr * repeat
        else:
            stack[-1][0] += c
    return stack[0][0]