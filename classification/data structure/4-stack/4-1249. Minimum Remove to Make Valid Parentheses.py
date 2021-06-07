'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
'''

def minRemoveToMakeValid(s):
    dels = set()
    stack = []
    for i, c in enumerate(s):
        if stack and c == ')':
            stack.pop()
        elif not stack and c == ')':
            dels.add(i)
        elif c == '(':
            stack.append(i)
    if stack:
        dels.update(set(stack))

    ans = ""
    for i, c in enumerate(s):
        if i in dels: continue
        ans += c
    return ans