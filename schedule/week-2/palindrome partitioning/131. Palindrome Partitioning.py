#coding=utf-8

'''
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

#用part == part[::-1]判断回文，没必要单独写函数
#注意审题，不是返回每个回文子串的集合，而是回文子串列表构成的集合
#对当前输入列表(字符串)进行切片，作为下一层的递归输入

def partition(s):

    #deprecated
    def ispalin(part):
        l,r = 0, len(part)-1
        if r == -1: return False
        while l < r:
            if part[l] != part[r]: return False
            l += 1
            r -= 1
        return True

    def _helper(curs, part, ret):
        if not curs:
            ret += part,
            return

        i,n = 1,len(curs)
        while i<=n:
            if curs[:i] == curs[:i][::-1]:
                _helper(curs[i:], part+[curs[:i]], ret)
            i += 1

    ret = []
    _helper(s, [], ret)
    return ret

s = "aab"
print(partition(s))