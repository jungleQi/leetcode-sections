'''
You have k lists of sorted integers in ascending order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
'''

def smallestRange(A):
    ans = -1e9, 1e9
    for right in sorted(set(x for l in A for x in l), reverse=True):
        for B in A:
            while B and B[-1] > right:
                B.pop()
            if not B: return ans
        left = min(B[-1] for B in A)
        if right-left <= ans[1]-ans[0]:
            ans = left, right
    return ans


A = [[4,10,15,24,26]]
print(smallestRange(A))