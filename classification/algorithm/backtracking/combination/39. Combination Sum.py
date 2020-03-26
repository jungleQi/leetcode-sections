#coding=utf-8
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
 find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

def combinationSum(candidates, target):
    def _helper(cands, tar, path, ret):
        if tar == 0:
            ret.append(path)

        for i,can in enumerate(cands):
            #pruning
            if can > tar: return
            _helper(cands[i:] ,tar-can, path+[can], ret)

    if not candidates: return []

    ret = []
    #prepare for pruning
    candidates.sort()
    _helper(candidates, target, [], ret)
    return ret

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))