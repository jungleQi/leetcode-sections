#coding=utf-8

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    # keypoints:
    # 1.移动M*N次
    # 2.seen[i][j]，记录(i,j)是否已经访问过
    # 3.每次移动依据当前位移。位移的更新，依据当前边的索引值.
    #  dr = [0,1,0,-1], dc = [1,0,-1,0]，决定移动的方向
    if not matrix: return []
    R, C = len(matrix), len(matrix[0])
    visitor = [[False] * C for _ in range(R)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    ri = ci = di = 0

    ans = []
    for _ in range(R * C):
        visitor[ri][ci] = True
        ans.append(matrix[ri][ci])
        cr = ri + dr[di]
        cc = ci + dc[di]

        if 0 <= cr < R and 0 <= cc < C and not visitor[cr][cc]:
            ri, ci = cr, cc
        else:
            di = (di + 1) % 4
            ri = ri + dr[di]
            ci = ci + dc[di]
    return ans