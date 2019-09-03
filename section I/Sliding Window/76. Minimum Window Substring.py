def minWindow(s, t):
    from collections import Counter
    t_dict = Counter(t)

    formed, required = 0, len(t_dict)
    l,r = 0,0
    window_counter = {}
    ans = float("inf"), None, None

    while r<len(s):
        char = s[r]
        window_counter[char] = window_counter.get(char, 0) + 1

        if char in t_dict and window_counter[char] == t_dict[char]:
            formed += 1

        while formed == required:
            if ans[0] > r-l+1:
                ans = (r-l+1, l, r)

            window_counter[s[l]] -= 1
            if s[l] in t_dict and window_counter[s[l]] < t_dict[s[l]]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
