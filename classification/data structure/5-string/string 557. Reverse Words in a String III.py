#coding=utf-8

# 入栈：遇到字符
# 出栈：遇到whitespace
def reverseWords_stack(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    ans = []

    # pad " " to trigger last stack pop
    for c in s + " ":
        if c == ' ':
            while stack:
                ans.append(stack.pop())
            ans.append(c)
        else:
            stack.append(c)

    return "".join(ans[:-1])

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    return " ".join([i[::-1] for i in s.split()])