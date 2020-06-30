#coding=utf-8

'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

#native:  没有用list记录窗口内的元素值， 因为这样查找会使用[i:j].find()操作，导致效率很低，类似于嵌套一层循环
#optimize:采用dict记录访问过的元素及其索引，这样查找元素非常高效，因为dict内部实现是hash查找;
#         再用start来记录窗口起始索引，为了避免每次滑动窗口需要更新窗口内元素对应的dict，可以采用
#         if c in sdict and sdict[c]>=start 来判断当前元素是否在滑动窗口内，这一步显得非常grace!
#         每次访问新元素时，将新元素索引更新到sdict就可以了

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    visitor = {}
    left = 0
    maxLen = 0
    for i, c in enumerate(s):
        if c in visitor and visitor[c] >= left:
            left = visitor[c] + 1

        visitor[c] = i
        maxLen = max(maxLen, i - left + 1)
    return maxLen