def monotoneIncreasingDigits(N):
    arr = [int(c) for c in str(N)]
    nLen = len(arr)

    curidx,latestConvertIdx = 0, nLen
    for curidx in range(nLen-2, -1, -1):
        if arr[curidx] > arr[curidx+1]:
            latestConvertIdx = curidx+1
            arr[curidx] = arr[curidx]-1

    resArr = [9]*(nLen-latestConvertIdx)
    if arr[curidx] != 0:
        res = arr[:latestConvertIdx] + resArr
    else:
        res = resArr

    ret = [str(i) for i in res]
    return int("".join(ret)) if ret else 0

N = 2220 #101
print monotoneIncreasingDigits(N)