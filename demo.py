def calculate(s):
    s = '('+s+')'
    stack = []
    i,n =0, len(s)
    while i<n:
        if s[i] in '+-(':
            stack.append(s[i])
        elif s[i].isdigit():
            numstr = ""
            while i<n and s[i].isdigit():
                numstr += s[i]
                i+=1
            stack.append(int(numstr))
            i -= 1
        elif s[i] == ')':
            cursum = 0
            while stack:
                top = stack.pop()
                if stack and stack[-1] == '+':
                    cursum += top
                    stack.pop()
                elif stack and stack[-1] == '-':
                    cursum -= top
                    stack.pop()
                elif stack and stack[-1] == '(':
                    cursum += top
                    stack[-1] = cursum
                    break
        i += 1

    return stack[-1]


def calculate_II(s):
    def update(op, num):
        if op == '+':
            stack.append(num)
        elif op == '-':
            stack.append(-num)
        elif op == '*':
            stack.append(stack.pop()*num)
        elif op == '/':
            stack.append(int(float(stack.pop())/num))

    i,n = 0,len(s)
    op,curnum = '+',0
    stack = []
    while i<n:
        if s[i].isdigit():
            curnum = curnum*10+int(s[i])
        elif s[i] in "+-*/":
            update(op, curnum)
            curnum = 0
            op = s[i]
        i += 1
    update(op,curnum)
    print(stack)
    return sum(stack)


def calculate_III(s):
    stack = []
    num,res,sign = 0,0,1
    i,n = 0, len(s)

    while i<n:
        if s[i].isdigit():
            num = 10*num+int(s[i])
        elif s[i] in '+-':
            res += num*sign
            num = 0
            sign = 1 if s[i] == '+' else -1
        elif s[i] == '(':
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif s[i] == ')':
            res += num * sign
            res = res*stack.pop() + stack.pop()
            sign = 1
            num = 0
        i += 1

    return res+num*sign

s = "(1+(4+5+2)-3)+(6+8)"
print(calculate_III(s))