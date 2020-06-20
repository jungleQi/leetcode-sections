#coding=utf-8

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

        #对corner case进行补充
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