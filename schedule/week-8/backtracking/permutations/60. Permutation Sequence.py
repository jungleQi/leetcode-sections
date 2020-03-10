#coding=utf-8

'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Input: n = 3, k = 3
Output: "213"
'''

#用递归回溯来处理，会超时是O(n!)
#有规律可寻，就采用推导的方式O(n).

outpath = ""
index = 0
def getPermutation_II_TLE(n, k):
    res = []
    def _helper(cands, num, path):
        global index
        if num == 0:
            index = index+1
            if index == k:
                res.append(path)
                return True
            else:
                return False

        for i,cand in enumerate(cands):
            ret = _helper(cands[:i]+cands[i+1:], num-1, path+cand)
            if ret == True: return True

        return False

    candidates = [str(i + 1) for i in range(n)]
    _helper(candidates, n, "")
    return res[0]

def getPermutation(n, k):
    fac = [1]
    for i in range(1,n+1):
        fac.append(fac[-1]*i)

    cands = [str(i) for i in range(1,n+1)]

    path = []
    cnt = n-1
    for i in range(n):
        idx = (k-1)//fac[cnt]
        k = k%fac[cnt]
        path.append(cands[idx])
        cands.remove(cands[idx])
        cnt -= 1
    return "".join(path)

print(getPermutation(3,3))
#print(getPermutation(9,199269))