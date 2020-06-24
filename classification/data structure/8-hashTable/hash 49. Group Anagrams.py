'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
1.All inputs will be in lowercase.
2.The order of your output does not matter.
'''

import collections
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    sdict = collections.defaultdict(list)
    for cur in strs:
        sdict["".join(sorted(cur))].append(cur)

    return sdict.values()
