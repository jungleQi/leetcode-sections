def findKthNumber(m, n, k):
    def compWithK(mid):
        cnt = 0
        for i in range(1, m+1):
            cnt += min(n, mid//i)
            if cnt >= k:
                return 1
        return -1

    lo = 1
    hi = m*n
    while lo < hi:
        mid = (lo+hi)//2
        ret = compWithK(mid)
        #print(lo, mid,hi, ret)
        if ret == 1:
            hi = mid
        else:
            lo = mid+1

    return lo

print findKthNumber(2, 2, 2)

