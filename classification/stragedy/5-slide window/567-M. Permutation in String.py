import collections
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    n = len(s1)
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2[:n])

    for i in range(n, len(s2)):
        if c1 == c2: return True

        if s2[i] in c2:
            c2[s2[i]] += 1
        else:
            c2[s2[i]] = 1

        if c2[s2[i - n]] <= 1:
            del c2[s2[i - n]]
        else:
            c2[s2[i - n]] -= 1

    return c1 == c2