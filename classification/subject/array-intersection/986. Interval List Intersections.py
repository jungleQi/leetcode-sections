#coding=utf-8

'''
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
 The intersection of two closed intervals is a set of real numbers that is either empty,
 or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
'''

#1.为了得到intersection区域，重用pair比较模块，让比较函数的参数传入固定，调用比较函数时
#  按照参数规则，调整传入参数的顺序
#2.当前哪个pair的右边界更小，就递增它对应的索引变量，这是关键

def intervalIntersection(A, B):
    def get_intersection(pair1, pair2):
        if pair2[0] > pair1[1]:
            return []
        elif pair2[1] <= pair1[1]:
            return pair2
        else:
            return [pair2[0], pair1[1]]

    ans = []
    i, j = 0, 0
    M, N = len(A), len(B)
    while i < M and j < N:
        if A[i][0] <= B[j][0]:
            ret = get_intersection(A[i], B[j])
        else:
            ret = get_intersection(B[j], A[i])

        if ret: ans.append(ret)
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return ans

def intervalIntersection_concise(A, B):
    ans = []
    i = j = 0

    while i < len(A) and j < len(B):
        # Let's check if A[i] intersects B[j].
        # lo - the startpoint of the intersection
        # hi - the endpoint of the intersection
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            ans.append([lo, hi])

        # Remove the interval with the smallest endpoint
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return ans

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(intervalIntersection(A, B))
