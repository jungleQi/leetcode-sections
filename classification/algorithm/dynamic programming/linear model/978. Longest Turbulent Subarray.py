def maxTurbulenceSize(A):
    N = len(A)
    if N == 1: return 1

    curLen, maxLen, i= 1, 1, 2
    if A[0] != A[1]: curLen = maxLen = 2

    while i < N:
        prod = (A[i]-A[i-1])*(A[i-1]-A[i-2])
        if prod<0:
            curLen += 1
        elif A[i]== A[i-1]:
            curLen = 1
        else:
            curLen = 2
        maxLen = max(maxLen, curLen)
        i += 1
    return maxLen

A = [4,4,42,4,4]
print(maxTurbulenceSize(A))