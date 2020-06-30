#coding=utf-8

import collections
def lengthOfLongestSubstringTwoDistinct(s):
    """
    :type s: str
    :rtype: int
    """
    #BAD: 采用三个变量，分别控制不同索引值，每次依据不同的情况去更新三个遍历，互让逻辑变得非常复杂，不清晰
    # 0 最左侧索引， 1 第一个元素最后的索引， 2 第二个元素最后的索引

    #GOOD: 用dict保存已经遍历过的字符key:字符 val:字符索引，再次访问字典存储的字符后
    # 更新对应的索引(为当前最大索引)，如果dict长度>=3就要删除掉索引值最小的i元素，并更新left = i+1

    hashmap = collections.defaultdict(int)
    left = ans = 0
    for i, c in enumerate(s):
        hashmap[c] = i

        if len(hashmap) >= 3:
            idx = min(hashmap.values())
            del hashmap[s[idx]]
            # 因为hashmap的更新规律与特点，这里直接+1处理，就能得到下一个字符的起始索引值
            left = idx + 1

        ans = max(ans, i - left + 1)
    return ans



