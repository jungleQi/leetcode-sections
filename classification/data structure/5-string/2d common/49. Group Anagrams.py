def groupAnagrams(strs):
    import collections
    sdict = collections.defaultdict(list)
    for i,str in enumerate(strs):
        sdict["".join(sorted(str))].append(str)

    res = []
    for k, curstrs in sdict.items():
        res += curstrs,

    return res

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)