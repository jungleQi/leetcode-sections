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

global outpath, isFind
outpath = ""
isFind= False
index = 0

def getPermutation(n, k):
    def _helper(candidates, n, k, path):
        global isFind, outpath, index

        if isFind: return
        if n == 0 :
            index += 1
            if index == k:
                isFind = True
                outpath = path
            return

        for idx,num in enumerate(candidates):
            _helper(candidates[:idx]+candidates[idx+1:], n-1, k, path+str(num))

    candidates = [i+1 for i in range(n)]
    _helper(candidates, n, k, "")
    return outpath

print(getPermutation(3, 3))