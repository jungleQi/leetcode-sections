import math

def numSquarefulPerms(A):
    def edge(x, y):
        r = math.sqrt(x + y)
        return int(r + 0.5) ** 2 == x + y

    def dfs(A, result, results):
        if not A:
            results += result,
            return

        prev = A[0]+1
        for idx, num in enumerate(A):
            if prev == num: continue
            prev = num
            if not result or edge(num, result[-1]):
                dfs(A[:idx]+A[idx+1:], result+[num], results)

    A.sort()
    results= []
    dfs(A, [], results)
    return  results

A = [1,17,8,2]
ret = numSquarefulPerms(A)
print(ret)

