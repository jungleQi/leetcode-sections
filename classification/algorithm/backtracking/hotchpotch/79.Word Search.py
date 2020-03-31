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

def exist(board, word):
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