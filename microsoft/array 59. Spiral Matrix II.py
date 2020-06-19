#coding=utf-8

def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    ans = [[0] * n for _ in range(n)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    di = 0
    i, j = 0, 0
    for num in range(1, n * n + 1):
        #填充的位置很重要，放在第一步处理
        ans[i][j] = num

        ni, nj = i + dr[di], j + dc[di]
        if ni >= n or nj >= n or ni < 0 or nj < 0 or ans[ni][nj] > 0:
            di = (di + 1) % 4

        i, j = i + dr[di], j + dc[di]

    return ans