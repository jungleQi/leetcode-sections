def numsSameConsecDiff_recursive(N, K):
    def _help(n, curnum, numstr,res):
        if n == 0:
            res.append(int(numstr))
            return

        for i in range(0,10):
            if n == N:
                if i > 0 or N == 1:
                    _help(n-1, i, str(i), res)
            elif abs(curnum-i) == K:
                _help(n-1, i, numstr+str(i), res)

    res = []
    _help(N, 0, "", res)
    return res

N = 1
K = 0
print numsSameConsecDiff_recursive(N, K)
