'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:
Input: "()"
Output: 1

Example 2:
Input: "(())"
Output: 2
'''

def scoreOfParentheses(s):
    stack = [0]
    for c in s:
        if c == '(':
            stack.append(0)
        else:
            top = stack.pop()
            if top == 0:
                stack[-1] += 1
            else:
                stack[-1] += top*2
    return stack[0]

S = "((()()))"
print(scoreOfParentheses(S))
