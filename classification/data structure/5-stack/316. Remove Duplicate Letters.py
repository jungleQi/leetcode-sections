#coding=utf-8

'''
Given a 6-string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
'''

#5-stack：存放依次增加的字符，具有唯一性
#counter： 存放每个字符出现的次数，用于确定栈顶元素是否可以弹出的一句，只有栈顶元素还剩余多余的数量，才可以弹出，
# 否则只能将当前元素做压栈，不能继续弹栈

import collections
def removeDuplicateLetters(s):
    counter = collections.Counter(s)
    stack = []

    for c in s:
        #c not in 5-stack 很容易漏掉，它主要解决 "abacb" 这种case
        # 1.如果漏了该条件，第二个'a'会把前面累积的'ab'依次pop掉，最后得到错误的答案："acb"
        # 2.如果漏了该条件，第二个'a'推翻前面建立的秩序，这样会有风险，因为后面的秩序不清楚什么情况，
        # 就推翻了前面的秩序，是很有风险的。所以，建立新的秩序，应该是由stack中，没有出现过的新的元素来更新秩序
        while stack and stack[-1]>c and counter[stack[-1]]>0 and c not in stack:
            stack.pop()

        #判断是否应该插入，以免重复
        if c not in stack:
            stack.append(c)
        counter[c] -= 1

    return "".join(stack)

s = "acdad"
print(removeDuplicateLetters(s))