def decodeAtIndex(S, K):
    curlen = 0
    for c in S:
        if c.isdigit():
            curlen = int(c)*curlen
        else:
            curlen += 1

    for c in reversed(S):
        K = K % curlen
        if K == 0 and c.isalpha():
            return c

        if c.isdigit():
            curlen = curlen / int(c)
        else:
            curlen -= 1

S = "a2345678999999999999999"
K = 1
print decodeAtIndex(S, K)