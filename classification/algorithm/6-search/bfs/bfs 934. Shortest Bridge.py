import collections
def shortestBridge(A):
    # DFS & BFS
    row = len(A)
    col = len(A[0])
    q = collections.deque()

    def exploreIsland(r, c):
        if not 0 <= r < row or not 0 <= c < col or A[r][c] == -1:
            return
        if A[r][c] == 1:
            A[r][c] = -1
            exploreIsland(r - 1, c)
            exploreIsland(r + 1, c)
            exploreIsland(r, c + 1)
            exploreIsland(r, c - 1)
        elif A[r][c] == 0:
            q.append((r, c, 1))

    def findFirst():
        for r in range(row):
            for c in range(col):
                if A[r][c] == 1:
                    exploreIsland(r, c)
                    return

    findFirst()
    # q = collections.deque([findFirst(1)])
    while q:
        cur_r, cur_c, cur_l = q.popleft()
        for x, y in ((cur_r + 1, cur_c), (cur_r - 1, cur_c), (cur_r, cur_c + 1), (cur_r, cur_c - 1)):
            if 0 <= x < row and 0 <= y < col:
                if A[x][y] == 1:
                    return cur_l
                elif A[x][y] == 0:
                    A[x][y] = -1
                    q.append((x, y, cur_l + 1))