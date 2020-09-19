def advantageCount(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    b_i = []
    for i, n in enumerate(B):
        b_i.append([n,i])
    sort_b_i = sorted(b_i, key=lambda x: x[0])
    A.sort()

    ans = ['']*len(A)
    noSelected = []
    curIdx = 0
    for i, n in enumerate(A):
        if n>sort_b_i[curIdx][0]:
            ans[sort_b_i[curIdx][1]] = n
            curIdx += 1
        else:
            noSelected.append(n)

    idx = 0
    for i, c in enumerate(ans):
        if c == '':
            ans[i] = noSelected[idx]
            idx += 1
    return ans

A = [8,2,4,4,5,6,6,0,4,7]
B = [0,8,7,4,4,2,8,5,2,0]
print advantageCount(A, B)
print [4,7,8,6,5,4,0,6,4,2]