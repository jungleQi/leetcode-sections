import math

def kthSmallestPrimeFraction(A, K):
    err = 1e-9
    def smaller(AA, lens, val):
        cnt = 0
        for i in range(1, lens):
            lo = 0
            hi = i-1
            while lo<hi:
                mid = (lo+hi+1)//2
                #land on bigger between two
                if AA[mid]*1.0/AA[i]<val:
                    lo = mid
                else:
                    hi = mid-1
            if A[lo]*1.0/A[i] < val:
                cnt += lo + 1
            else:
                cnt += lo
                print(lo, hi, A[lo], A[i])
            #cnt += lo+1 if A[lo]/A[i] < val else lo

        return cnt

    lens = len(A)
    lo = 1.0/A[-1]
    hi = (A[-1]-1.0)/A[-1]
    while hi-lo > err:
        mid = (hi+lo)/2.0
        cnt = smaller(A, lens, mid)
        #approach to real fraction as many as possible
        if cnt > K-1:
            hi = mid
        else:
            lo = mid

    print(lo)
    for i in range(lens):
        p = int(math.floor(A[i]*lo+0.5))
        #print(p, A[i], abs(p/A[i]-lo))
        if (p < A[i]) and (p in A) and (abs(p*1.0/A[i]-lo) < err):
            return [p,A[i]]

    return []

A = [1,2,11,37,83,89]
K = 3
print(kthSmallestPrimeFraction(A, K))