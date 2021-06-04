'''
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.


Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
'''

def reverseParentheses_my(s):
    stack = [["(", ""]]
    for c in s:
        if c == '(':
            stack.append(['(', ""])
        elif c == ')':
            if stack[-1][0] == '(':
                stack[-1][1] = stack[-1][1][::-1]

            top = stack.pop()
            stack[-1][1] += top[1]
        else:
            stack[-1][1] += c

    return stack[0][1]

def reverseParentheses_official(s):
    stack = ['']

    for ch in s:
        if ch == '(':
            stack.append('')
        elif ch == ')':
            tmp = stack.pop()[::-1]
            stack[-1] += tmp
        else:
            stack[-1] += ch

    return ''.join(stack)

s = "a(bcdefghijkl(mno)p)q"
print(reverseParentheses_official(s))