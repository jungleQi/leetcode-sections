#log(N)
def sortedSquares(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    idx = 0
    N = len(A)
    for n in A:
        if n < 0:
            idx += 1
        else:
            break

    i = idx - 1
    ans = []
    while idx < N and i >= 0:
        if -A[i] < A[idx]:
            ans.append(A[i] * A[i])
            i -= 1
        else:
            ans.append(A[idx] * A[idx])
            idx += 1

    if idx < N:
        ans += [n * n for n in A[idx:]]
    elif i >= 0:
        ans += [n * n for n in A[i::-1]]

    return ans