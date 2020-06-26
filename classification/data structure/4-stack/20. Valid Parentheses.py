#coding=utf-8

'''
Given a 5-string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input 5-string is valid.

An input 5-string is valid if:
    1.Open brackets must be closed by the same type of brackets.
    2.Open brackets must be closed in the correct order.
Note that an empty 5-string is also considered valid.

Example 1:

Input: "([)]"
Output: false
'''

#4-stack：三对括弧，采用字典的映射关系来访问，很concise

def isValid(s):
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        else:
            if stack :
                top = stack.pop()
                if not ((c==')' and top=='(') or (c=='}' and top=='{') or (c==']' and top=='[')):
                    return False
            else:
                return False
    return True if not stack else False

def isValid_usingDict(s):
    stack = []
    cdict = {']':'[',')':'(','}':'{'}

    for c in s:
        if c in cdict.values():
            stack.append(c)
        else:
            if not stack or cdict[c] != stack.pop():
                return False
    return len(stack) == 0


s = "["
print(isValid_usingDict(s))