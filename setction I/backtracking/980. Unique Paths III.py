def uniquePathsIII(grid):
    zeroNum = 0
    row = len(grid)
    col = len(grid[0])

    visitor = [[0]*col for _ in range(row)]
    startRow, startCol = 0,0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                zeroNum += 1
            elif grid[i][j] == 1:
                startRow , startCol = i, j

    paths = set()
    def dfs(zeroNum, i,j, visitor, path):
        if i < 0 or i >= row or j < 0 or j >= col:
            return False

        if zeroNum == -1 and grid[i][j] == 2:
            curt = tuple(path)
            paths.add(curt)
            return True

        if visitor[i][j] == 1 or grid[i][j] != 0 or zeroNum < -1:
            return False

        visitor[i][j] = 1
        for item in [[i,j-1], [i,j+1], [i-1,j], [i+1,j]]:
            dfs(zeroNum-1, item[0], item[1], visitor, path+[tuple(item)])
        visitor[i][j] = 0

    grid[startRow][startCol] = 0
    dfs(zeroNum, startRow, startCol,visitor, [])
    return len(paths)

#grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
grid = [[0,1],[2,0]]
print uniquePathsIII(grid)