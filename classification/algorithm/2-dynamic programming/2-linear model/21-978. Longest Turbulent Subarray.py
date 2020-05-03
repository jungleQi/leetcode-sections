#coding=utf-8

'''
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

Example 1:
Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
'''

# lightspot :
# cmp返回值为 A, B之间大小关系，1: A>B, 0: A==B, -1: A<B
# 不用连续的if elif else 来判断

def maxTurbulenceSize(A):
    maxLen, curLen, preOpt = 1, 1, 0
    for i in range(1, len(A)):

        c = cmp(A[i], A[i - 1])
        if (c>0 and preOpt == -1) or (c<0 and preOpt == 1):
            curLen += 1
        else:
            curLen = 1 + abs(c)

        preOpt = c
        maxLen = max(maxLen, curLen)

    return maxLen

A = [4,4,42,4,4]
print(maxTurbulenceSize(A))