'''
We have an 7-array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B,
obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)
'''
def subarrayBitwiseORs(A):
    ans = set()
    cur = {0}
    for x in A:
        cur = {x|y for y in cur} | {x}
        ans |= cur
    return len(ans)

A = [1,1,2]
print(subarrayBitwiseORs(A))