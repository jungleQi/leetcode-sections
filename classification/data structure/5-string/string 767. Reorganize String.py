#coding=utf-8

def reorganizeString(S):
    """
    :type S: str
    :rtype: str
    """
    N = len(S)
    A = []
    for i, c in sorted((S.count(x), x) for x in set(S)):
        #异常情况就直接返回
        if i > (N + 1) / 2: return ""
        A.extend(i * c)

    ans = [None] * N
    #这里赋值是本题的灵魂
    ans[::2], ans[1::2] = A[N / 2:], A[:N / 2]

    return "".join(ans)