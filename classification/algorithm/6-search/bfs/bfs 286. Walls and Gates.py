import collections
def wallsAndGates(rooms):
    """
    :type rooms: List[List[int]]
    :rtype: None Do not return anything, modify rooms in-place instead.
    """
    if not rooms: return
    M, N = len(rooms), len(rooms[0])
    neigbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(i, j):
        deque = collections.deque([(i, j, 0)])
        while deque:
            x, y, d = deque.popleft()
            for nei in neigbors:
                if x + nei[0] < 0 or x + nei[0] >= M or y + nei[1] < 0 or y + nei[1] >= N or \
                        rooms[x + nei[0]][y + nei[1]] == -1 or \
                        rooms[x + nei[0]][y + nei[1]] <= d:
                    continue

                rooms[x + nei[0]][y + nei[1]] = d + 1
                deque.append((x + nei[0], y + nei[1], d + 1))


    for i in range(M):
        for j in range(N):
            if rooms[i][j] == 0:
                bfs(i, j)