def calculate(s):
    stack = []
    prevStr = ""
    curStr = ""
    curNum = 0
    prevOpt = ''
    for c in s:
        if c.isdigit():
            curStr += c
            if prevOpt == '*':
                curNum = int(prevStr)*int(curStr)
            elif prevOpt == '/':
                curNum = int(prevStr)//int(curStr)
            else:
                curNum = int(curStr)
        elif c == '+' or c == '-':
            stack.append(curNum)
            stack.append(c)
            prevOpt = ''
            curStr = ""
        elif c == '*' or c == '/':
            prevOpt = c
            prevStr = str(curNum)
            curStr = ""
    stack.append(curNum)

    ret = 0
    opt = ''
    for i in stack:
        if i not in ['+','-']:
            if opt == '':
                ret = i
            elif opt == '+':
                ret += i
            else:
                ret -= i
        else:
            opt = i

    return ret

s = " 3+5 / 2 "
print(calculate(s))