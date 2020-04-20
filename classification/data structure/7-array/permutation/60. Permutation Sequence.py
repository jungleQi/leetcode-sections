def getPermutation(n, k):
    nums = [i+1 for i in range(n)]
    facbs = {}
    for i in range(1,n+1):
        if i == 1:
            facbs[i] = 1
        else:
            facbs[i] = facbs[i-1]*i

    ret = []
    for i in range(1,n):
        if k < 0:
            break
        idx = k/facbs[n-i]
        ret += nums[idx],
        del nums[idx]

        k -= facbs[n-i]*idx
        k = k % facbs[n - i]
    strret = [str(i) for i in ret]
    return "".join(strret)


print getPermutation(3, 3)
exit(1)









def getPermutation2(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    fac = [1]
    nums = [1]
    for i in range(1, n):
        fac.insert(0, fac[0] * i)
        nums.append(i + 1)

    res = ""
    for i in range(n):
        nidx = (k - 1) / fac[i]
        res += str(nums[nidx])
        del nums[nidx]
        k = k % fac[i]

    return res


ret = getPermutation(9,219601)

#ret = getPermutation(0,1)
print(ret)

