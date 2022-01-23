'''
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
'''

def calculate(s):
    # op is num's prev-operator
    def update(op, num):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(num*stack.pop())
        elif op == '/':
            stack.append(int(float(stack.pop())/num))

    op, num = "+", 0
    s += "+"
    stack = []
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c in ('+','-','*','/'):
            update(op, num)
            op = c
            num = 0

    return sum(stack)

s = "3-5/4"
print(calculate(s))