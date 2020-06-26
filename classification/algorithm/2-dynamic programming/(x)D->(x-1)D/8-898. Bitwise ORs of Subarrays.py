'''
We have an 2-array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B,
obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)
'''

import collections

#1360 ms
def subarrayBitwiseORs_spaceComplex(self, A):
    dp = collections.defaultdict(set)
    ans = set()
    for i, n in enumerate(A):
        dp[i].add(n)
        for m in dp[i - 1]:
            dp[i] |= {n | m}

        ans |= dp[i]
    return len(ans)

#864 ms
def subarrayBitwiseORs(A):
    ans = set()
    cur = {0}
    for x in A:
        cur = {x|y for y in cur} | {x}
        ans |= cur
    return len(ans)

A = [1,1,2]
print(subarrayBitwiseORs(A))