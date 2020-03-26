'''
You have a set of tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make.

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
'''

import collections
def numTilePossibilities_counter(tiles):
    counter = collections.Counter(tiles)

    def dfs(ret):
        if sum(counter.values()) == 0:
            return
        for c, n in counter.items():
            if n == 0: continue
            ret[0] += 1
            counter[c] -= 1
            dfs(ret)
            counter[c] += 1

    ret = [0]
    dfs(ret)
    return ret[0]

def numTilePossibilities_set(tiles):
    def helper(srctiles, path):
        if not srctiles: return
        for i in range(len(srctiles)):
            helper(srctiles[:i]+srctiles[i+1:], path+srctiles[i])
            res.add(path+srctiles[i])

    res = set()
    helper(tiles, "")
    return len(res)


tiles = "AAB"
print(numTilePossibilities_set(tiles))
