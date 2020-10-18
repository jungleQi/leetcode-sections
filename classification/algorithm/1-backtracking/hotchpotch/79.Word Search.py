#coding=utf-8

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


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

def exist_II(board, word):
    M = len(board)
    N = len(board[0])

    def travel(i,j,path, idx, visitor):
        if path == word:
            return True

        neighbor = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
        for row, col in neighbor:
            if row >= M or col >= N or row < 0 or col < 0:
                continue

            #pruning
            if board[row][col] != word[idx] or visitor[row][col]:
                continue

            visitor[row][col] = True
            ret = travel(row, col, path+board[row][col], idx+1, visitor)
            visitor[row][col] = False
            if ret: return True

        return False

    visitor = [[False]*N for _ in range(M)]
    for m in range(M):
        for n in range(N):
            if board[m][n] == word[0]:
                visitor[m][n] = True
                ans = travel(m, n, word[0], 1, visitor)
                visitor[m][n] = False
                if ans: return True
    return False

board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word = "ABCB"
print(exist(board, word))