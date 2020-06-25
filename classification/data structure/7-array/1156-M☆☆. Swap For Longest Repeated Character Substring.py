#coding=utf-8

'''
Given a string text, we are allowed to swap two of the characters in the string.
Find the length of the longest substring with repeated characters.

Example 1:
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'.
Then, the longest repeated character substring is "aaa", which its length is 3.
'''

import collections
def maxRepOpt1(text):
    """
    :type text: str
    :rtype: int
    """
    # 细节上处理的不好，导致程序写不出来
    # 区分处理 连续性的substring 和 间隔性的substring
    # 在一个流程中处理兼容两种情况，会有很大困难
    def getLongest(v):
        #prev前一个连续区间的长度，curr当前连续区间的长度
        prev, curr = 0, 1
        sum_res = 0

        # 主流程处理艺术：处理主干case
        for i in range(len(v) - 1):
            if v[i + 1] - v[i] <= 1:
                curr += 1
            else:
                if v[i + 1] - v[i] == 2:
                    prev = curr
                else:
                    prev = 0
                curr = 1
            sum_res = max(sum_res, prev + curr)

        #除了corner case(整个v区间都是连续)，对其他情况下的长度需要补充空缺的1
        if sum_res < len(v):
            sum_res += 1

        return sum_res

    cdict = collections.defaultdict(list)
    for i, c in enumerate(text):
        cdict[c].append(i)

    ans = 1
    for k, arr in cdict.items():
        ans = max(ans, getLongest(arr))
    return ans