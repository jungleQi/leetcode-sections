import collections
def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """

    N = len(s1)
    src = collections.Counter(s1)

    dst = collections.Counter(s2[:N])
    if src == dst: return True

    l = 0
    for r in range(N, len(s2)):
        if s2[r] != s2[l]:
            dst[s2[l]] -= 1
            if dst[s2[l]] <= 0:
                del dst[s2[l]]

            if s2[r] not in dst:
                dst[s2[r]] = 1
            else:
                dst[s2[r]] += 1
        l += 1
        if src == dst: return True
    return False