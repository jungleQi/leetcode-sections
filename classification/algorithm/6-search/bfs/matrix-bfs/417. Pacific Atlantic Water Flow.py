#coding=utf-8

'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
(从某个起始点出发都存在满足条件的路径，list就是这些起始点的集合)

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''

#在一定遍历限制条件下，哪些点能够到达目的地(指定规则的)

#广度优先，采用deque方式，无法记录深度路径

#寻找哪些元素满足条件：
# 1.如果对每个元素进行扩展，寻找它是否满足条件，就加入到答案，
#   这种方式是在黑暗中逆向查找，会很低效~~

# 2.如果已知一些已经满足条件的元素，将其加入队列，按照BFS的方式扩展，将其领域满足条件的元素全都加入到答案，
#   这种方式是在光明中正想查找，会非常高效！！

import collections

def pacificAtlantic_slow(matrix):
    goPac, goAtl = set(), set()
    M,N = len(matrix), len(matrix[0])
    directions= [[-1,0],[1,0],[0,-1],[0,1]]

    for i in range(M):
        for j in range(N):
            q = collections.deque()
            q.append((i,j))
            visitor = set()
            while q:
                x,y = q.popleft()
                for dir in directions:
                    row,col = x+dir[0],y+dir[1]

                    if row<0 or col<0 :
                        goPac.add((i,j))
                    elif row>=M or col>=N :
                        goAtl.add((i,j))
                    elif matrix[row][col]<=matrix[x][y]:
                        if (row,col) in goPac:
                            goPac.add((i, j))
                        if (row,col) in goAtl:
                            goAtl.add((i,j))
                        if (row, col) not in goPac and (row, col) not in goAtl and (row, col) not in visitor:
                            q.append((row,col))
                            visitor.add((row,col))
    ret = []
    for item in goPac:
        if item in goAtl:
            ret.append(item)
    return ret


def pacificAtlantic(matrix):
    if not matrix: return []
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    m,n = len(matrix), len(matrix[0])

    def bfs(ocean_found):
        q = collections.deque(ocean_found)
        while q:
            i,j = q.popleft()
            for r,c in directions:
                if i+r>=0 and i+r<m and j+c>=0 and j+c<n \
                    and matrix[i+r][j+c]>=matrix[i][j] and (i+r,j+c) not in ocean_found:
                    ocean_found.add((i+r,j+c))
                    q.append((i+r,j+c))
        return ocean_found

    pac = set([(i,0) for i in range(m)] + [(0,j) for j in range(n)])
    atl = set([(i,n-1)for i in range(m)] + [(m-1,j) for j in range(n)])
    return bfs(pac) & bfs(atl)

matrix = [[1,2,2,3,5],
          [3,2,3,4,4],
          [2,4,5,3,1],
          [6,7,1,4,5],
          [5,1,1,2,4]]
print(pacificAtlantic(matrix))