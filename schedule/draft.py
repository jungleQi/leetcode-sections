def partition(s):
    def helper(s, comb, ret):
        if not s:
            ret.append(comb)
            return

        for i in range(1,len(s)+1):
            subs = s[:i]
            if subs == subs[::-1]:
                helper(s[i:], comb+[subs], ret)

    ret = []
    helper(s, [], ret)
    return ret

s = ""
print(partition(s))
