def longestOnes(A, K):
    oneCnt, start, end = 0, 0, 0
    maxLen = 0
    while end<len(A):
        oneCnt += A[end]

        end += 1
        if end-start-oneCnt <= K:
            maxLen = max(maxLen, end-start)

        while end-start-oneCnt > K:
            oneCnt -= A[start]
            start += 1
    return maxLen

A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(longestOnes(A, K))