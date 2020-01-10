'''
Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord, such that:
1.Only one letter can be changed at a time
2.Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.
'''

import string,sys
import collections

def findLadders_TLE(beginWord, endWord, wordList):
    wordList = set(wordList)

    minlen = sys.maxsize
    ans = []
    ls = string.ascii_lowercase
    queue = [(beginWord, 1, [beginWord])]
    while queue:
        word, length, curpath = queue.pop(0)
        if word == endWord:
            if length <= minlen:
                ans.append(curpath)
                minlen = length
            else:
                return ans

        for i in range(len(word)):
            for j in ls:
                newword = word[:i]+j+word[i+1:]
                if newword in wordList and newword not in curpath:
                    queue.append((newword, length+1, {newword}.union(curpath)))

    return ans

def findLadders_old(beginword, endword, wordlist):
    if endword not in wordlist:
        return []
    forward = {beginword}
    backward = {endword}
    parents = collections.defaultdict(set)
    direction = 1

    wordlist = set(wordlist)
    while forward and backward:
        next_forward = set()
        if len(forward) > len(backward):
            forward, backward = backward, forward
            direction = -direction

        wordlist = wordlist - forward
        for word in forward:
            for i in range(len(word)):
                first, second = word[:i], word[i + 1:]
                for ch in string.ascii_lowercase:
                    newword = first + ch + second
                    if newword in wordlist:
                        next_forward.add(newword)

                        if direction == 1:
                            parents[newword].add(word)
                        else:
                            parents[word].add(newword)

        if next_forward & backward:
            results = [[endword]]
            while results[0][0] != beginword:
                results = [[parent] + result for result in results for parent in parents[result[0]]]
            return results
        forward = next_forward
    return []

def findLadders_submission(beginWord, endWord, wordList):

    # Create Wordmap for neighboring words
    tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
    if endWord not in wordList: return []

    found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
    while bq and not found:
        words -= set(bq)
        for x in bq:
            for y in [x[:i] + c + x[i + 1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
                if y in words:
                    if y in eq:
                        found = True
                    else:
                        nq.add(y)
                    tree[y].add(x) if rev else tree[x].add(y)
        bq, nq = nq, set()
        if len(bq) > len(eq):
            bq, eq, rev = eq, bq, not rev

    def bt(x):
        return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]

    return bt(beginWord)



beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(findLadders(beginWord, endWord, wordList))