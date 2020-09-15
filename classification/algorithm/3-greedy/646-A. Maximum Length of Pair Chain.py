'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs.
You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

Note:
The number of given pairs will be in the range [1, 1000].

'''

def findLongestChain(pairs):
    curTail, pairCnt = float('-inf'),0
    for pair in sorted(pairs, key=lambda x:x[1]):
        if pair[0]>curTail:
            curTail = pair[1]
            pairCnt += 1
    return pairCnt

def findLongestChain_FromLeftToRight(pairs):
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    pairs.sort(key=lambda x: x[0])

    chainCnt = 0
    leftest = pairs[0][0] - 1
    for pair in pairs:
        if pair[0] > leftest:
            chainCnt += 1
            leftest = pair[1]
        else:
            leftest = min(leftest, pair[1])
    return chainCnt

pairs = [[1,2], [2,3], [3,4]]
print(findLongestChain(pairs))