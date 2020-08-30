'''
Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).

Note:
1.The length of the given string is ≤ 10000.
2.Each number will contain only one digit.
3.The conditional expressions group right-to-left (as usual in most languages).
4.The condition will always be either T or F. That is, the condition will never be a digit.
5.The result of the expression will always evaluate to either a digit 0-9, T or F.

Example 1:
Input: "T?2:3"
Output: "2"
Explanation: If true, then result is 2; otherwise result is 3.

Example 2:
Input: "F?1:T?4:5"
Output: "4"
'''

#routine:
def parseTernary(expression):
    stack = []
    i = len(expression) - 1
    while i >= 0:
        if expression[i].isdigit() or expression[i] in 'TF':
            stack.append(expression[i])
        elif expression[i] == '?':
            first = stack.pop()
            second = stack.pop()
            i = i - 1
            if expression[i] == 'T':
                stack.append(first)
            else:
                stack.append(second)
        i -= 1
    return stack[-1] if stack else ""

expression = ""
print(parseTernary(expression))




