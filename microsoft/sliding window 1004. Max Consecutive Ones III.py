def longestOnes(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    start = end = oneCnt = 0
    N = len(A)

    maxLen = 0
    while end < N:
        oneCnt += A[end]
        end += 1

        if end - start - oneCnt <= K:
            maxLen = max(maxLen, end - start)
        else:
            oneCnt -= A[start]
            start += 1

    return maxLen