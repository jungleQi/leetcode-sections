#coding=utf-8

import collections
def maxLength(arr):
    """
    :type arr: List[str]
    :rtype: int
    """
    conts = []
    for curstr in arr:
        counter = collections.Counter(curstr)

        #对单个字符串进行判断
        if len(counter) != len(curstr):
            continue

        for cont in conts:
            comb = True
            for k in counter.keys():
                if k in cont:
                    comb = False
                    break

            #是否能对当前积累的cont集合进行扩充
            if comb == False: continue

            #保留原有的set，赋值一份对其进行扩充
            newCont = cont.copy()
            for k in counter.keys():
                newCont.add(k)
            conts.append(newCont)

        conts.append(set(counter.keys()))

    #
    maxlen = 0
    for item in conts:
        maxlen = max(maxlen, len(item))
    return maxlen