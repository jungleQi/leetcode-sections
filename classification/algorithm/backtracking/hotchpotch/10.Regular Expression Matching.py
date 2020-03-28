#coding=utf-8

'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

'''

#关键是怎么对p中*的处理 ： 对*可能的作用，形成多个分支，构建解空间树
#难点在于：选择什么时机作为回溯点，如何进行不同分支解的展开，如何结束返回的问题
#分析:1. '*'只会影响到它前一个字符的行为，不同的影响行为，分别建立一个解分支
#    2. 如何返回：
#       s空，p不一定为空也可能是true，判断起来比较麻烦；
#       p为空，s为空就true，不为空就false。这个得益于isMatch(s, p[2:])

def isMatch(s, p):
    if not p:
        return not s

    first_match = bool(s) and p[0] in ('.', s[0])
    if len(p)>=2 and p[1] == '*':
        return isMatch(s, p[2:]) or (first_match and isMatch(s[1:], p))
    else:
        return first_match and isMatch(s[1:], p[1:])

s = ""
p = "s*s*i*"
print(isMatch(s, p))