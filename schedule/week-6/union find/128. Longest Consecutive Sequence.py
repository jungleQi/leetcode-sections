#coding=utf-8

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

    #
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


#时间复杂度为O(n)
# the numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups
# we only attempt to build sequences from numbers that are not already part of a longer sequence
def longestConsecutive_n(nums):
    numsSet = set(nums)
    longestStreak = 1

    for num in numsSet:
        if num-1 in numsSet:
            continue

        curStreak = 1
        curNum = num+1
        while curNum in numsSet:
            curStreak += 1
            curNum += 1
        longestStreak = max(longestStreak, curStreak)
    return longestStreak

nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive_n(nums))