#coding=utf-8

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

#stack: 将 '(', '+', '-'，数字单元 都入栈，当遇到 ')'时，开始做出栈运算
#为了便于处理原始字符串s首尾没有'(', ')'，最后栈内可能存余多个需要计算的数字
#非常trick的做法，是在原始字符串s首尾，分别添加'(', ')'，这样可以利用遇到')'时触发的出栈运算
#最后stack只剩余一个元素，就是最后运算的结果

def calculate(s):
    s = s.strip()
    if not s: return 0
    #trick and smart operation
    s = '('+s+')'

    stack = []
    i, N = 0, len(s)
    while i < N:
        if s[i] in ['(', '+', '-']:
            stack.append(s[i])
        elif s[i].isdigit():
            numStr = ""
            while i < N and s[i].isdigit():
                numStr += s[i]
                i += 1
            stack.append(int(numStr))
            i -= 1
        elif s[i] == ')':
            cursum = 0
            while stack:
                top = stack.pop()
                if stack and stack[-1] == '-':
                    cursum -= top
                    stack.pop()
                elif stack and stack[-1] == '+':
                    cursum += top
                    stack.pop()
                elif stack and stack[-1] == '(':
                    cursum += top
                    stack[-1] = cursum
                    break
        i += 1
    return stack[0]

s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s))
