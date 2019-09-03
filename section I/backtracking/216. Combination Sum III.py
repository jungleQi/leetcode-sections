def combinationSum3(k, n):
    candidates = [i for i in range(1,10)]
    solutions = []
    def DFS(target, cnt, idx, res):
        if target == 0 and cnt == 0:
            solutions.append(res)
            return

        for i in xrange(idx+1, 9):
            if candidates[i] <= target:
                DFS(target-candidates[i], cnt-1, i, res+[candidates[i]])
            else:
                return

    DFS(n, k, -1, [])
    return solutions

print(combinationSum3(1,9))