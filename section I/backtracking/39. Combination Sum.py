
def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    solution = []
    def DFS(target, cnt, res, idx):
        if target == 0:
            solution.append(res[:])
            return

        for i in xrange(idx, cnt):
            if candidates[i] <= target:
                res.append(candidates[i])
                DFS(target-candidates[i], cnt, res, i)
                res.pop()
            else:
                return

    candidates.sort()
    cnt = len(candidates)
    DFS(target, cnt, [], 0)
    return solution

candidates = []
target = 8
print combinationSum(candidates, target)