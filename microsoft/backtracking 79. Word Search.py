#coding=utf-8

# keypoint:
# 1. 遍历M*N，以每个元素为起始点，开始dfs
# 2. dfs采用回溯，几个变量控制搜索：visitor, directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# 3. 如果当前path == word，结束遍历

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """

    R, C = len(board), len(board[0])
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    seen = [[False] * C for _ in range(R)]

    def backtracking(i, j, path, length):
        if i < 0 or i >= R or j < 0 or j >= C or path != word[:length]:
            # print path, word[:length]
            return False

        # print path
        if path == word:
            return True

        for direction in directions:
            di, dj = i + direction[0], j + direction[1]
            if di < 0 or di >= R or dj < 0 or dj >= C or seen[di][dj]:
                continue

            seen[di][dj] = True
            if backtracking(di, dj, path + board[di][dj], length + 1):
                return True
            seen[di][dj] = False
        return False

    for row in range(R):
        for col in range(C):
            seen[row][col] = True
            if backtracking(row, col, board[row][col], 1):
                return True
            seen[row][col] = False
    return False