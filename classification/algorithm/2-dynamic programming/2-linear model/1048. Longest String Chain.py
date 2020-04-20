'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.
 For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2,
 word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

'''

import collections
def longestStrChain(words):
    word_seg = collections.defaultdict(list)
    for word in words:
        word_seg[len(word)].append(word)
    sort_word_seg = sorted(word_seg.items(), key=lambda x:(x[0], x[1]))

    i,N = 1,len(sort_word_seg)
    length_word = collections.defaultdict(lambda :1)
    while i<N:
        if len(sort_word_seg[i][1][0]) - len(sort_word_seg[i-1][1][0]) > 1:
            i += 1
            continue

        for w1 in sort_word_seg[i][1]:
            for j in range(len(w1)):
                delword = w1[:j] + w1[j+1:]
                if delword in sort_word_seg[i-1][1]:
                    length_word[w1] = max(length_word[w1], length_word[delword]+1)
        i += 1

    return max(length_word.values()) if length_word else 1

words = ["a","b","ab","caaa", "caba","caada","cacaaa"]
print(longestStrChain(words))

