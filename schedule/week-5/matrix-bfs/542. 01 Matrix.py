#coding=utf-8

'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
'''

#每个点都会遍历四个方向，有可能相邻的两个点来回互相访问，导致死循环，如何避免这点
#1.记录visitor；
#2.初始化dist所有值，通过dist邻域的值判断是否访问过，
#  如果没有访问或者访问之后发现值是不如当前最新的值，就更新邻域值，而且将邻域这个坐标放入queue，
#  寻求对领域的领域的访问和值的判断与更新

import collections

def updateMatrix(matrix):
    M, N = len(matrix), len(matrix[0])
    ret = [[0 for _ in range(N)] for _ in range(M)]

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0: continue

            q = collections.deque()
            q.append((i, j, 0))
            visitor = set()
            while q:
                x, y, dist = q.popleft()
                visitor.add((x, y))
                for dir in direction:
                    ln, col = x + dir[0], y + dir[1]
                    if ln < 0 or ln >= M or col < 0 or col >= N or (ln, col) in visitor: continue

                    if matrix[ln][col] == 0:
                        ret[i][j] = dist + 1
                        break
                    elif matrix[ln][col] == 1:
                        q.append((ln, col, dist + 1))
                if ret[i][j] > 0: break
    return ret

import sys
def updateMatrix_submission(matrix):
    M,N = len(matrix), len(matrix[0])
    dist = [[sys.maxint for _ in range(N)] for _ in range(M)]

    q = collections.deque()
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 0:
                dist[i][j] = 0
                q.append((i,j))

    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    while q:
        x,y = q.popleft()
        for dir in directions:
            row,col = x+dir[0],y+dir[1]
            if row <0 or row>=M or col<0 or col>=N or dist[row][col]<=dist[x][y]+1:
                continue

            dist[row][col] = dist[x][y]+1
            q.append((row,col))

    return dist

matrix = [[1,1,1,0,0],[1,1,1,1,0],[1,0,0,0,1]]
ret = updateMatrix_submission(matrix)
for col in ret: print(col)


