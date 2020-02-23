'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class UF(object):
    def __init__(self, n):
        self.N = n
        self.parent = range(n)

    def find(self,i):
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        self.parent[ri] = rj

    def maxUnion(self):
        count = [0]*self.N
        ret = 0
        for i in range(self.N):
            root = self.find(i)
            #print(i, root)
            count[root] += 1
            ret = max(ret, count[root])
        return ret

def longestConsecutive(nums):
    map = dict()
    uf = UF(len(nums))

    for i, n in enumerate(nums):
        if n in map: continue
        map[n] = i
        if n+1 in map:
            uf.union(i, map[n+1])
        if n-1 in map:
            uf.union(i, map[n-1])

    return uf.maxUnion()


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))