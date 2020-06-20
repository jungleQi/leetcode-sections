#coding=utf-8

import collections, heapq
def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    counter = collections.Counter(words)
    #根据题意，频率最高的word，频率相同按照lexicon升序排列，所以下面采用了很巧妙的方式
    kFreq = heapq.nsmallest(k, counter.items(), key=lambda x: (-x[1], x[0]))
    #而不是直接按照题意，如果这样就是lexicon降序排列
    #kFreq = heapq.nlargest(k, counter.items(), key=lambda x: (x[1], x[0]))

    return zip(*kFreq)[0]