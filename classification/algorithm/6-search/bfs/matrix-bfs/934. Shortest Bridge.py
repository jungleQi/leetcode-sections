import collections

#1.队列元素：初始状态下，包含了某个island所有的元素(边缘+内陆)
#2.向外扩张：因为队列里，各种元素的掺杂，边缘的扩展虽然是按距离非递减加入，但是加入的过程不平滑，会因很多内陆元素的出现踩空
#3.队列元素的意义不单一，初始状态是island，后来就变成了海水，让原始矩阵每个元素值更新，理解起来不是很自然
def shortestBridge_fakeBFS(A):
    R, C = len(A), len(A[0])
    q = collections.deque()

    def dfs(A, i, j):
        if i>=R or i<0 or j>=C or j<0 or A[i][j] == 0 or A[i][j] == -1:
            return

        A[i][j] = -1
        q.append((i,j,1))
        dfs(A, i+1, j)
        dfs(A, i - 1, j)
        dfs(A, i, j+1)
        dfs(A, i, j-1)

    def findFirst():
        for i in range(R):
            for j in range(C):
                if(A[i][j] == 1):
                    dfs(A, i, j)
                    return

    findFirst()
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    minSlip = R+C

    while q:
        r,c,d = q.popleft()
        for i,j in directions:
            if(r+i>=R or r+i<0 or c+j>=R or c+j<0 or A[r+i][c+j]==-1): continue
            if(A[r+i][c+j] > 1 and A[r+i][c+j] <= d+1): continue

            if(A[r+i][c+j]==1):
                minSlip = min(minSlip, d)
            else:
                A[r + i][c + j] = d + 1
                q.append((r + i, c + j, d + 1))
    return minSlip-1


#1.列队元素：初始状态下，只包含某个island的第一层海水元素
#2.向外扩张：因为是按照海水元素的离岸距离进行入列，所以队列的出列和入列显得非常平滑清晰
#3.队列元素的意义单一，一直都是海水元素(带了离岸距离)，原始矩阵每个元素值更新很简单，遍历过的填充为island元素
def shortestBridge_realBFS(A):
    # DFS & BFS
    R, C = len(A), len(A[0])
    q = collections.deque()

    def dfs(A, i, j):
        if i >= R or i < 0 or j >= C or j < 0 or A[i][j] == -1:
            return

        if A[i][j] == 1:
            A[i][j] = -1
            dfs(A, i + 1, j)
            dfs(A, i - 1, j)
            dfs(A, i, j + 1)
            dfs(A, i, j - 1)
        elif A[i][j] == 0:
            q.append((i, j, 1))

    def findFirst():
        for i in range(R):
            for j in range(C):
                if (A[i][j] == 1):
                    dfs(A, i, j)
                    return

    findFirst()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        r, c, d = q.popleft()
        for i, j in directions:
            if (r + i >= R or r + i < 0 or c + j >= C or c + j < 0 or A[r + i][c + j] == -1): continue

            if (A[r + i][c + j] == 1):
                return d
            else:
                q.append((r + i, c + j, d + 1))
                A[r + i][c + j] = -1