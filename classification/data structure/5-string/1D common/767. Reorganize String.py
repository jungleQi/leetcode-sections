
def reorganizeString(S):
    N = len(S)
    A = []
    for i,x in sorted((S.count(x), x) for x in set(S)):
        if i > (N+1)//2: return ""
        A.extend([x]*i)

    ans = [None]*N
    ans[::2] = A[N//2:]
    ans[1::2] = A[:N//2]
    return "".join(ans)

S = "aabbcca"
print(reorganizeString(S))