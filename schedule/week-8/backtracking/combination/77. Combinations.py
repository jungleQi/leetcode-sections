#coding=utf-8

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
'''

#记录下一层递归的起始索引值，能很大的提升递归效率

def combine_slow(n, k):
    def _helper(candidates, k, path, ret):
        if k == 0:
            ret += path,
            return

        for can in candidates:
            if path and path[-1] >= can: continue
            _helper(candidates, k-1, path+[can], ret)

    candidates = [i for i in range(1,n+1)]
    ret = []
    _helper(candidates, k, [], ret)
    return ret

def combine_efficent(n, k):
    def _helper(candidates, start, n, k, path, ret):
        if k == 0:
            ret += path,
            return

        while start <= n-k :
            _helper(candidates, start+1, n, k-1, path+[candidates[start]], ret)
            start += 1

    candidates = [i for i in range(1, n + 1)]
    ret = []
    _helper(candidates, 0, n, k, [], ret)
    return ret

n,k = 4,2
print(combine_efficent(n, k))