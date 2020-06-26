def firstUniqChar(s):
    from collections import Counter

    counter = Counter(s)
    for i, c in enumerate(s):
        if counter[c] == 1:
            return i

    return -1


s = "ltl"
print(firstUniqChar(s))