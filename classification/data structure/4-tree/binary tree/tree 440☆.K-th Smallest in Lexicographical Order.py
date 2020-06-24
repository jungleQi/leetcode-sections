#coding=utf-8

#十叉树问题，如果采用先序遍历
def findKthNumber(n, k):
    def calSteps(n, n1, n2):
        step = 0
        while n1 <= n:
            step += min(n + 1, n2) - n1
            n1 = n1 * 10
            n2 = n2 * 10
        return step

    curr = 1
    k = k - 1
    while k > 0:
        step = calSteps(n, curr, curr + 1)
        if step <= k:
            k -= step
            curr += 1
        else:
            curr = curr * 10
            k -= 1
    return curr