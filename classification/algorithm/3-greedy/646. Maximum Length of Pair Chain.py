'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs.
You can select pairs in any order.
'''

def findLongestChain(pairs):
    curTail, pairCnt = float('-inf'),0
    for pair in sorted(pairs, key=lambda x:x[1]):
        if pair[0]>curTail:
            curTail = pair[1]
            pairCnt += 1
    return pairCnt

pairs = [[1,2], [2,3], [3,4]]
print(findLongestChain(pairs))