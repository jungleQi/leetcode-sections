def combinationSum2(candidates, target):
    def helper(cands, target, path, ret):
        if target == 0:
            ret.append(path)
            return

        for i,cand in enumerate(cands):
            if cand>target:
                return
            if i>0 and cands[i-1] == cand:
                continue
            helper(cands[i+1:], target-cand, path+[cand], ret)

    ans = []
    candidates.sort()
    helper(candidates, target, [], ans)
    return ans

candidates = [2,5,2,1,2]
target = 5
print(combinationSum2(candidates, target))

