'''
Find all possible combinations of k numbers that add up to a number n,
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Input: k = 3, n = 7
Output: [[1,2,4]]
'''

def combinationSum3(k, n):
    def _helper(k, n, candidates, path, ret):
        if k == 0 and n == 0:
            ret += path,
            return

        for can in candidates:
            if can>n: break
            #make sure unique number in combination and no duplicate combination
            if path and path[-1]>=can: continue

            _helper(k-1,n-can, candidates, path+[can], ret)

    candidates = [i for i in range(1,10)]
    ret = []
    _helper(k,n,candidates,[],ret)
    return ret

def combinationSum3_II(k, n):
    def _helper(cands, k, n, path, ret):
        if k == 0 and n == 0:
            ret.append(path)
            return
        for i, can in enumerate(cands):
            if can > n or (path and path[-1] > n): break
            _helper(cands[i + 1:], k - 1, n - can, path + [can], ret)

    ret = []
    candidates = [i + 1 for i in range(9)]
    _helper(candidates, k, n, [], ret)
    return ret

k,n = 3, 9
print(combinationSum3_II(k, n))