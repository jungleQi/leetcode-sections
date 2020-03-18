#coding=utf-8

'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

'''


import heapq, collections
def topKFrequent_submission(words, k):
    count = collections.Counter(words)
    #建堆时，对于节点是元组时，如果第一个元素相等，会以第二个元素的大小为依据进行建堆
    #heapq是小顶堆
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in xrange(k)]

def test():
    nums = [(1,"c"),(1,"b"),(2,"d"),(2,"a")]
    heapq.heapify(nums)
    print([heapq.heappop(nums)[1] for _ in xrange(4)])
    print(nums)

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
#print(topKFrequent(words, k))
test()