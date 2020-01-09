#coding=utf-8

'''
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

1.Only one letter can be changed at a time.
2.Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''

#这才是真正的BFS
#避免LTE 判断字符是否在list中，用 a in list判断，会非常慢导致超时，一般对list -> set，然后用 a in set，
# 这时候是基于hash查找，会比较快，另外对已经访问过的a，用set.remove(a)也是比较高效

import collections

def ladderLength_TLE(beginWord, endWord, wordList):
    queue = [(beginWord, 1)]
    visited = set()

    while queue:
        word, dist = queue.pop(0)
        if word == endWord:
            return dist
        for i in range(len(word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                tmp = word[:i] + j + word[i + 1:]
                if tmp not in visited and tmp in wordList:
                    queue.append((tmp, dist + 1))
                    visited.add(tmp)
    return 0


def ladderLength_pass(beginWord, endWord, wordList):
    wordList = set(wordList)
    queue = collections.deque([[beginWord, 1]])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append([next_word, length + 1])
    return 0


beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(ladderLength_pass(beginWord, endWord, wordList))
