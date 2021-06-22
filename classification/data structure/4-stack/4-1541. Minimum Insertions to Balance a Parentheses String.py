'''
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as openning parenthesis and '))' as closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.


Example 1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching.
We need to to add one more ')' at the end of the string to be "(())))" which is balanced.
'''

def minInsertions(s):
    stack = []
    i = res = 0
    while i < len(s):
        if s[i] == '(':
            stack.append('(')
        else:
            if not stack:
                res += 1
                stack.append('')  # padding

            if i < len(s) - 1 and s[i + 1] == ')':
                i += 1
            else:
                res += 1
            stack.pop()

        i += 1
    return res + len(stack) * 2


s = ")))"
print(minInsertions(s))