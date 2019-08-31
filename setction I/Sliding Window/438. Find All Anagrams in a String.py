def findAnagrams(s, p):
    from collections import Counter
    def is_Same(sd, pd):
        isSame = True
        for k, v in pd.items():
            if sd[k] != v:
                isSame = False
                break
        return isSame

    res = []
    M, N = len(p), len(s)
    if M > N: return res

    start , end = 1, M
    p_dict = Counter(p)
    s_dict = Counter(s[:end])

    isSame = False
    if len(p_dict) == len(s_dict) and is_Same(s_dict, p_dict):
        isSame = True
        res.append(0)

    while end < N:
        if isSame and s[end] == s[start-1]:
            res.append(start)
        else:
            s_dict[s[start-1]] -= 1
            s_dict[s[end]] += 1
            isSame = is_Same(s_dict, p_dict)
            if isSame:
                res.append(start)

        start += 1
        end += 1

    return res

s ="b"
p = "ab"
print findAnagrams(s, p)
