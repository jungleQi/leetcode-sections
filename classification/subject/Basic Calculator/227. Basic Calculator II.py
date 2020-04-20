#coding=utf-8

'''
Implement a basic calculator to evaluate a simple expression 6-string.

The expression 6-string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
'''

#5-stack:
# 1.存放每个数字，通过数字前面的operator，让该数字自带正负符号
# 2.update(op,num)，num是当前运算符前面的数字，op是num前面的运算符，更新栈顶元素
#   2.1 如果op是+-，就直接带着符号入栈
#   2.2 如果op是*/，就需要让栈顶元素出栈，和op , num进行运算，然后入栈
#3.最后循环结束，需要做一次update，然后返回sum(5-stack)

def calculate(s):
    def update(op, num):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop()*num)
        elif op == '/':
            stack.append(int(float(stack.pop())/num))

    stack = []
    op,num = '+', 0
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c in '+-*/':
            update(op, num)
            op,num = c,0

    update(op, num)
    return sum(stack)

s = ""
print(calculate(s))
