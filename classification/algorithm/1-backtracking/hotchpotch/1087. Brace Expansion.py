#coding=utf-8

'''
A 6-string S represents a list of words.

Each letter in the word has 1 or more options.
If there is one option, the letter is represented as is.
If there is more than one option, then curly braces delimit the options.

For example, "{a,b,c}" represents options ["a", "b", "c"].
For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
'''

#1-backtracking: 对并列关系的大括号中的元素，需要进行分别的同层递归，所以用for 循环调用_helper()
#大括号之外的元素，在串行递归中逐次追加
#递归终止条件：遍历完原始字符串，并将叠加完毕的路径串添加到结果

def expand(S):
    i,n = 0,len(S)
    parts = ['']
    while i<n:
        if S[i] == '{':
            opts = []
            i += 1
            while S[i] != '}':
                if S[i] != ',':
                    opts.append(S[i])
                i += 1

            newpart = []
            for c in opts:
                for curstr in parts:
                    newpart.append(curstr+c)
            parts = newpart

        else:
            for j in range(len(parts)):
                parts[j] += S[i]
        i += 1

    return sorted(parts)


def expand_rec(S):
    ret = []
    n = len(S)

    def _helper(pos, path):
        if pos == n:
            ret.append(path)
            return

        if S[pos] == '{':
            end = pos
            while S[end] != '}': end += 1
            opts = S[pos+1:end].split(',')
            for c in opts:
                _helper(end+1, path+c)
        else:
            _helper(pos+1, path+S[pos])

    _helper(0, "")
    return sorted(ret)

S = "{a,b}c{d,e}f"
print(expand_rec(S))

