#coding=utf-8

'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
'''


#[0,0]*n的形式，会导致n个[0,0]都是同一个对象，导致后续复制的错误

#超时的解法：对每个0进行bfs，将遍历到的所有的1的路径长度加起来，得到它的遍历长度，和之前最小的遍历长度对比，得到全局的最小长度

#pass解法：
# 1.从每个building为起点，进行bfs，遍历完毕如果它不能遍历到所有buildings，就返回-1，这是pruning
# 2.利用vistor防止重复访问
# 3.每个空地(0)都记录它被访问的次数，代表了有几个building 为起点的bfs能够访问到它
# 4.每个空地(0)都记录每次被访问的步长，代表了某个building到它的最短路径长度
# 5.重复1.2.3.4步骤，完成所有的building为起点的bfs后， 比较能到达所有buliding的空地(0)，
#   它的总步长和当前最小总步长的长度，从而得到返回最小值

import sys,collections,copy
def shortestDistance_TLE(grid):
    mindist = sys.maxint
    m,n = len(grid), len(grid[0])

    buildings = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0: continue

            distsum = 0
            curbuildings = copy.copy(buildings)

            q = collections.deque()
            q.append((i,j,0))

            visitor = set()
            visitor.add((i, j))
            while q and curbuildings:
                x,y,d = q.popleft()
                for r,c in directions:
                    row,col = x+r,y+c
                    if row<0 or row>=m or col<0 or col>=n or grid[row][col] == 2 or (row,col) in visitor:
                        continue

                    if grid[row][col] == 1:
                        distsum += d+1
                        curbuildings.remove((row,col))
                    else:
                        q.append((row,col,d+1))
                    visitor.add((row,col))
            if not curbuildings:
                print(i, j, distsum, curbuildings)
                mindist = min(mindist, distsum)
    return mindist if mindist != sys.maxint else -1


def shortestDistance(grid):
    if not grid or not grid[0]: return -1
    m,n,buildings = len(grid),len(grid[0]),sum(v for line in grid for v in line if v==1)
    hit = [[[0,0] for _ in range(n)] for _ in range(m)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    def bfs(start_x, start_y):
        buildVisitors, visitor = 1,[[False]*n for _ in range(m)]
        q = collections.deque([(start_x, start_y, 0)])
        visitor[start_x][start_y] = True

        while q:
            x,y,d = q.popleft()
            for dir in directions:
                row,col = x+dir[0],y+dir[1]
                if row<0 or row>=m or col<0 or col>=n or visitor[row][col]:
                    continue

                visitor[row][col] = True
                if grid[row][col] == 1:
                    buildVisitors += 1
                elif grid[row][col] == 0:
                    hit[row][col][0] += 1
                    hit[row][col][1] += d+1
                    q.append((row,col,d+1))
        return buildVisitors == buildings

    mindist = sys.maxint
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not bfs(i,j):
                return -1

    for i in range(m):
        for j in range(n):
            if grid[i][j] ==0 and hit[i][j][0] == buildings:
                mindist = min(mindist, hit[i][j][1])

    return mindist if mindist != sys.maxint else -1

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(shortestDistance(grid))