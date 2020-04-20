#coding=utf-8

'''
Implement a basic calculator to evaluate a simple expression 6-string.

The expression 6-string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

The expression 6-string contains only non-negative integers, +, -, *, / operators ,
open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
'''

#5-stack:
# 1.遇到数字字符，就累积到num；
# 2.遇到'('，让前面的那个operator字符入栈，op='+',num=0
# 3.遇到'+-*/)',就将它前面的num以及num前面的operator一起，
#   3.1 去更新栈；
#       3.1.1 如果operator是+-，就让num带上符号，入栈
#       3.1.2 如果operator是*/，它们计算优先级高，栈顶元素出栈，operator, num，三者一起计算新的值，再入栈
#   3.2 如果是 ')'，就连续叠加stack栈顶(弹出)元素，直至栈顶元素不是数字(为'('前面的operator)
# 4.最后将operator,num去更新栈

#KEY：
# 1.operator 和 num的更新时机(operator 是 num前面的运算符)
# 2.stack存放待运算的数字和'('之间的operator，每个数字有正负号，便于统一做加法
# 3.update(op, num)，用于更新栈顶元素
# 3.最后循环结束之后，需要将最后的operator 和 num，去更新stack栈顶元素

def calculate(s):
    """
    :type s: str
    :rtype: int
    """
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
    op, num = '+', 0
    for c in s:
        if c.isdigit():
            num = num*10+int(c)
        elif c in "+-*/)":
            update(op, num)
            if c == ')':
                num = 0
                while isinstance(stack[-1], int):
                    num += stack.pop()
                update(stack.pop(), num)
            num, op = 0, c
        elif c == '(':
            stack.append(op)
            num,op = 0,'+'

    update(op, num)
    return sum(stack)


#s = "-1+4*3/3/3"
s= " ( 2+6 * 3+5- (3*14/7+2)*5)+3 "
print(calculate(s))
