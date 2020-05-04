#coding=utf-8

'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.
 For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2,
 word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

'''

#1492 ms
def longestStrChain_raw(words):
    def predec(word1, word2):
        for i, c in enumerate(word2):
            if word1 == word2[:i] + word2[i + 1:]:
                return True
        return False

    N = len(words)
    dp = [1] * N

    words.sort(key=lambda x: len(x))
    for i in range(1, N):
        j = i - 1
        while j >= 0:
            dist = len(words[i]) - len(words[j])
            if dist == 1:
                if predec(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
            elif dist > 2:
                break
            j -= 1
    return max(dp) if dp else 0

#68 ms
#lightspot:
# 1.将原始数据重新组织成一个新的数据结构 bucket: [dict(), ... , dict()]，这非常有利于本问题的高效求解
# 2.将阶段从 原始数据 转换成 bucket的16个桶
# 3.dp[i]，表示以原始数据第i个字符串结尾的最长chain长度
# 4.所有阶段的求解，是以[2]为阶段来求解的，而不是以dp[0...i]里的索引值为阶段求解

def longestStrChain_grace(words):
    bucket = [dict() for _ in range(16)]
    for i, w in enumerate(words): bucket[len(w) - 1][w] = i

    dp = [1] * len(words)
    for i, buck in enumerate(bucket):
        if i == 0 or len(bucket) == 0 or len(bucket[i - 1]) == 0:
            continue

        prev = bucket[i - 1]
        for word in buck:
            idx = buck[word]

            for i in range(len(word)):
                sub = word[:i] + word[i + 1:]
                if sub in prev:
                    dp[idx] = max(dp[idx], dp[prev[sub]] + 1)

    return max(dp)


import collections
def longestStrChain_submission(words):
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

