#coding=utf-8

'''
Given an 2-array A of integers and integer K, return the maximum S
such that there exists i < j with A[i] + A[j] = S and S < K.
If no i, j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
'''

#normal:双层遍历，伺机退出第二层循环遍历，思路比较raw

#optimize:只需要单层遍历，判决循环层采用while l<r 的遍历方式，广泛适用于sum与target之间关系判断，从而求得结果

def twoSumLessThanK_slow(A, K):
    N = len(A)
    if N <= 1: return -1

    ret = []
    A.sort()
    for i in range(N-1):
        for j in range(i+1,N):
            if A[i]+A[j]>=K: break
            ret += A[i]+A[j],

    ret.sort(key=lambda x:K-x)
    return ret[0] if ret else -1

def twoSumLessThanK_fast(A, K):
    A.sort()
    l,r = 0,len(A)-1
    if r<1 or A[0]+A[1]>K:
        return -1

    maxLess = float('-inf')
    while l<r:
        curSum = A[l]+A[r]
        if curSum>=K:
            r -= 1
        else:
            if maxLess<curSum: maxLess = curSum
            l += 1
    return maxLess


A = [34,23,1,24,75,33,54,8]
K = 60
print(twoSumLessThanK_fast(A, K))