#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections


def longestStrChain(words):
    def predec(word1, word2):
        for i, c in enumerate(word2):
            if word1 == word2[:i]+word2[i+1:]:
                return True
        return False


    N = len(words)
    dp = [1]*N

    words.sort(key=lambda x: len(x))
    for i in range(1,N):
        j = i-1
        while j>=0:
            dist = len(words[i])-len(words[j])
            if dist == 0:
                j -= 1
            elif dist == 1:
                if predec(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
            else:
                break
            j -= 1
    return max(dp) if dp else 0

words = []
print longestStrChain(words)


