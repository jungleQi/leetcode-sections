def combine(n, k):
    def helper(iStart, n, k, result, results):
        if n-iStart < k :
            return
        if k == 0:
            results += result,
            return

        for i in range(iStart, n):
            helper(i+1, n, k-1, result+[i+1], results)

    results = []
    helper(0, n, k, [], results)
    return results


ret = combine(5,3)
print(ret)
