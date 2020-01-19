#coding=utf-8

'''
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

#关键：在candidate有重复元素时，如何过程中而不是添加时，控制住 unique combination

def combinationSum2(candidates, target):
    def _helper(start, end, tar, path, ret):
        if tar == 0 and path not in ret:
            ret += path,

        while start < end:
            if candidates[start] > tar: break
            can = candidates[start]
            _helper(start+1, end, tar-can, path+[can], ret)
            start += 1

    ret = []
    candidates.sort()
    _helper(0, len(candidates), target, [], ret)
    return ret

def combinationSum2_opt(candidates, target):
    def _helper(start, end, tar, path, ret):
        if tar == 0:
            ret += path,

        i = start
        while i < end:
            #make sure no duplicate combination
            if i > start and candidates[i] == candidates[i-1]:
                i += 1
                continue
            if candidates[i] > tar: break

            _helper(i+1, end, tar-candidates[i], path+[candidates[i]], ret)
            i += 1

    ret = []
    candidates.sort()
    _helper(0, len(candidates), target, [], ret)
    return ret

def combinationSum2_II(candidates, target):
    def _helper(cands, tar, path, ret):
        if tar == 0:
            ret.append(path)

        for i,can in enumerate(cands):
            if i>0 and cands[i-1] == can:
                continue
            if can > tar or (path and path[-1]>tar):
                break

            _helper(cands[i+1:],tar-can, path+[can], ret)

    ret = []
    candidates.sort()
    _helper(target, [], ret)
    return ret


target = 8
candidates = [10,1,2,7,6,1,5]
print(combinationSum2_opt(candidates, target))