'''
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2
'''

#如果有(就标识一下，表示后面这个数字不能做stack内的合并运算
# 20+12-(1-(4+5+20)-13)-(6-8)
def calculate(s):
    res = num = 0
    sign = 1
    stack = []

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in '+-':
            res += num * sign
            sign = (1 if c == '+' else -1)
            num = 0
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ')':
            res += num * sign
            res = res * stack.pop() + stack.pop()
            num = 0
    return res + num * sign
