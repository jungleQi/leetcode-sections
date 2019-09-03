import collections

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    m,n = len(board), len(board[0])
    if not m or not n:
        return False

    def dfs(i, j, path, s):
        if not s:
            return True

        if i<0 or i>= m or j<0 or j>=n:
            return False

        if board[i][j] != s[0] or (i,j) in path:
            return False

        path.add((i,j))
        for item in [[i,j-1], [i,j+1], [i-1,j], [i+1,j]]:
            if dfs(item[0], item[1], path, s[1:]):
                return True
        path.remove((i,j))
        return False

    c = collections.defaultdict(int)
    for i in range(m):
        for j in range(n):
            c[board[i][j]] += 1

    for s in word:
        if c[s] < 1:
            return False

    path = set()
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0] and dfs(i,j,path, word):
                return True
    return False

board = [["C","A","A"]]
print(exist(board, "AACD"))
