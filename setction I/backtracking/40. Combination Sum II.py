def combinationSum2(candidates, target):
    solution = []
    def DFS(target, idx, cnt, res):
        if target == 0:
            solution.append(res[:])
            return

        for i in xrange(idx+1, cnt):
            if candidates[i]<=target:
                if i==idx+1 or candidates[i] != candidates[i-1]:
                    DFS(target-candidates[i], i, cnt, res+[candidates[i]])
            else:
                return

    candidates.sort()
    cnt = len(candidates)
    DFS(target, -1, cnt, [])
    return solution

candidates = [10,1,2,7,6,1,5]
target = 8
print combinationSum2(candidates, target)