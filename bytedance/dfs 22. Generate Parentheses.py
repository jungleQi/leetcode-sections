#coding=utf-8

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    def dfs(l, r, path, ret):
        #注意此处条件，否则递归无法终止
        if l > r or l < 0 or r < 0: return
        if l == 0 and r == 0:
            ret.append(path)
            return
        dfs(l - 1, r, path + '(', ret)
        dfs(l, r - 1, path + ')', ret)

    ans = []
    dfs(n, n, "", ans)
    return ans
