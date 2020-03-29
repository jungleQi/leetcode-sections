#coding=utf-8

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

#1.画递归解空间树
#2.每个节点(回溯点)有几个分支，也就是需要调用几次递归
#3.递归传入参数的变化，包括计数递减、路径的累加
#4.控制好返回条件:
#  a.记录符合条件然后返回
#  b.pruning返回

def generateParenthesis(n):
    def helper(m,n,path, ret):
        if m == 0 and n == 0:
            ret.append(path)
            return
        if m<0 or n<0 or m>n: return

        helper(m-1, n, path+'(', ret)
        helper(m, n-1, path + ')', ret)

    ret = []
    helper(n, n ,"", ret)
    return ret

print(generateParenthesis(3))