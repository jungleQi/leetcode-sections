'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
 find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

def combinationSum_recursive(candidates, target):
    def _helper(start,end, remain, curCombination, ret):
        if remain == 0 :
            if curCombination not in ret:
                ret += curCombination,
            return
        if remain < 0: return

        while start<end:
            _helper(start, end, remain-candidates[start], curCombination+[candidates[start]],ret)
            start += 1

    ret = []
    _helper(0, len(candidates), target, [], ret)
    return ret

def combinationSum_backtracking(candidates, target):
    def _helper(tar, path, ret):
        if tar == 0:
            ret += path,

        for can in candidates:
            if can > tar: break
            if path and path[-1]>can:
                continue
            _helper(tar-can, path+[can], ret)

    candidates.sort()
    ret = []
    _helper(target, [], ret)
    return ret

def combinationSum(candidates, target):
    def _helper(cands, tar, path, ret):
        if tar == 0:
            ret.append(path)

        for i,can in enumerate(cands):
            if can > tar: break
            _helper(cands[i:] ,tar-can, path+[can], ret)

    if not candidates: return []

    ret = []
    candidates.sort()
    _helper(candidates, target, [], ret)
    return ret

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))