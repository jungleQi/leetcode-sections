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
    def helper(s, comb, ret):
        if not s:
            ret.append(comb)
            return

        for i in range(1, len(s) + 1):
            subs = s[:i]
            if subs == subs[::-1]:
                helper(s[i:], comb + [subs], ret)

    ret = []
    helper(s, [], ret)
    return ret

s = "aab"
print(partition(s))